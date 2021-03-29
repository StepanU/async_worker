## To run a program

### With Docker

```bash
docker-compose -p async-worker -f deploy/docker-compose.yml up -d --build
```

### Without Docker

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

## API endpoints

### worker

*POST* /worker/create

*GET* /worker/results

*GET* /worker/tasks

