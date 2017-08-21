# 授权Authorization

> 用以下代码指定Headers:

```shell
  # With shell, you can just pass the correct header with each request
  curl "<endpoint-url>" \
  -H "Authorization: <api-key>"
  -H "Accept: application/vnd.api+json"
```

```java
import java.io.*;
import java.net.*;

URL url = new URL("<endpoint-url>");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.setRequestMethod("GET");
conn.setRequestProperty("Authorization","<api-key>");
conn.setRequestProperty("Accept", "application/vnd.api+json");

conn.getInputStream()
```

```python
import requests

url = "<endpoint-url>"

header = {
    "Authorization": "<api-key>",
    "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
```

```ruby
```

```javascript
```

```go
import "net/http"

client := &http.Client{}
req, _ := http.NewRequest("GET","<endpoint-url>",nil)
req.Header.Set("Authorization", "<api-key>")
req.Header.Set("Accept", "application/vnd.api+json")
res, _ := client.Do(req)
```

我们需要您将您的JSON Web Token ([JWT](https://jwt.io/))与同 `Authorization` 一起发送。
JWTs会在授权（Authorization）头部中作为持有的token，外观如下：

`Authorization: <输入你的API key>`

您无需手动创建JWT，当您注册API时它会自动被创建。- [在这里注册！](https://developer.vainglorygame.com/users/sign_in)


有的时候 `X-API-KEY` 可以给你更多获取相关信息的权限，就一切情况而论，您是受token限制率规定限制的。