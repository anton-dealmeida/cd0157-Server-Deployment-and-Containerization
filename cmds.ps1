# curl --data '{"email":"abc@xyz.com","password":"mypwd"}' --header "Content-Type: application/json" -X POST localhost:8080/auth
$hostname = "a6e8a678c572245f28476a45ae06d9f8-2134729753.us-east-2.elb.amazonaws.com"

$param = @{
    Uri         = "$hostname/auth"
    Method      = "Post"
    Body        = '{"email":"abc@xyz.com","password":"mypwd"}'
    ContentType = "application/json"
}
$TOKEN = (Invoke-RestMethod @param).token

$headers = @{
    Authorization = "Bearer ${TOKEN}"
}

$param = @{
    Uri     = "$hostname/contents"
    Method  = "Get"
    Headers = $headers
}
$JSONObject = Invoke-RestMethod @param | ConvertTo-Json

echo $TOKEN
echo $JSONObject