Practice for setting up multiple Docker containers to be created from the same repo, sharing some common files.

Use:

```{bash}
cd modules
source .docker_build

# then to see what containers are doing, either:
docker run --rm engine
# or
docker run --rm backend
```
