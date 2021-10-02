# flask-sqlalchemy-x-ray-sample

A sample application to get started with Flask and AWS X-Ray integration

## Setup

1. Install x-ray daemon locally
2. Setup a Python virualenv and install requirements

```bash
python -m venv venv
pip install -r requirements.txt
```

3. Create .env file. A sample available at .env.sample
4. Start the application

```bash
python wsgi.py
```

5. Generate some traffic

```bash
for id in {100..110}; do
    curl -X POST "http://localhost/${id}"
    curl "http://localhost/${id}"
    sleep .25
done
```

6. Visit [AWS X-Ray Console](https://console.aws.amazon.com/xray/) and check the generated traces

## References

[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html)
[X-Ray SDK for Python middleware](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-middleware.html)
[Patching libraries to instrument downstream calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-patching.html)
[Generating custom subsegements](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-subsegments.html)
[AWS X-Ray Daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-local.html)
