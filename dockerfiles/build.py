import os

BANNED = ["build.py", "builds"]
EXECUTOR_COUNT = 4


def split_builds(builds, n):
    return [builds[i::n] for i in range(n)]


class Build:
    def __init__(self, name):
        self.name = name
        self.version = self.check_version()

    def check_version(self):
        if os.path.isfile(f"./{self.name}/.version"):
            with open(f"./{self.name}/.version", 'r') as file:
                return file.read()

        else:
            return "latest"

    def __repr__(self):
        return f"{self.name}, {self.version}"


locs = os.listdir(".")
builds = []
for loc in locs:
    if loc not in BANNED:
        builds.append(Build(loc))
split = split_builds(builds, EXECUTOR_COUNT)

for num, executor in enumerate(split):
    job_code = ""
    for build in executor:
        sh = (
            "set -e\n"
            f"docker login -u $DOCKER_USER -p $DOCKER_PASS\n"
            f"docker pull sharp6292/{build.name}:{build.version} || true\n"
            f"docker build --cache-from sharp6292/{build.name}:{build.version}"
            f" -f dockerfiles/{build.name}/Dockerfile "
            f"-t sharp6292/{build.name}:{build.version} .\n"
            f"docker push sharp6292/{build.name}:{build.version}\n"
        )
        job_code += sh
    with open(f'./builds/build-{num}.sh', 'w') as file:
        file.write(job_code)
