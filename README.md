Example for setting up multiple Docker images to be created from the same repo, sharing some common files.

- In this example, there are two Docker images created - `backend` and `engine`.
- Under `modules`, there are three sub-directories, `backend`, `common` and `engine`
- Both images have the working directory `modules` which contain both the `common` directory, plus their own directory (either `engine` or `backend`)

For example:
```
BACKEND IMAGE
- /
    - /modules/
        - common/
            - log_config.py
        - backend/
            - main_backend.py

ENGINE IMAGE
- /
    - /modules/
        - common/
            - log_config.py
        - engine/
            - main_engine.py
            - src/
                - calcs.py
```

The scripts in both backend and engine can be tested locally (use python3, no extra packages needed)
with either:
- `python3 -m backend.main_backend`
- `python3 -m engine.main_engine`

To confirm the same works when built and run as a Docker container:

```{bash}
cd modules
source .docker_build  # builds both backend and engine images

# then to see what containers are doing, either:
docker run --rm engine
# or
docker run --rm backend
```
