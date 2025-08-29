import json, os, uuid


CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",                # lub konkretny origin zamiast *
    "Access-Control-Allow-Methods": "POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type,Authorization",
}

def parse_json_body(event):
    data = json.loads(event.get("body") or "{}") 
    return data

def generate_key(event,data):
    ext = (data.get("ext") or "jpg").lower().lstrip(".")
    if ext == "jpeg": ext = "jpg"
    key = f"uploads/{uuid.uuid4()}.{ext}"
    return ext,key

def lambda_handler(event, context):
    bucket_name = os.environ.get("BUCKET_NAME", "not-set")
    message = "Hello from lambda-s3-geturl !!!"  
    data = parse_json_body(event)
    ext,key = generate_key(event, data)
    content_type = "image/jpeg" if ext == "jpg" else f"image/{ext}"
    body = {
        "message": message,
        "bucket": bucket_name,
        "s3_key": key,
        "got":data,
        "content_type":content_type
    }
    
    return {
        "statusCode": 200,
        "headers": {**CORS_HEADERS ,"Content-Type": "application/json"},
        "body": json.dumps(body)
    }