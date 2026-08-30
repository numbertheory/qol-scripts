# HTTP Status Codes

## 1xx Informational
100 Continue            Client should continue sending request body
101 Switching Protocols Upgrading protocol (e.g. HTTP to WebSocket)
103 Early Hints         Preload headers before final response

## 2xx Success
200 OK                  Standard success
201 Created             Resource created (check Location header)
202 Accepted            Queued for async/batch processing
204 No Content          Success, no body returned (DELETE/PUT)
206 Partial Content     Range request fulfilled (streaming/resuming)

## 3xx Redirection
301 Moved Permanently   Permanent; may rewrite POST -> GET
302 Found               Temporary; may rewrite POST -> GET
303 See Other           Redirect target must be retrieved with GET
304 Not Modified        Use cached version (ETag/If-None-Match)
307 Temporary Redirect  Temporary; PRESERVES request method & body
308 Permanent Redirect  Permanent; PRESERVES request method & body

## 4xx Client Error
400 Bad Request         Malformed syntax / invalid request
401 Unauthorized        Not authenticated (WWW-Authenticate required)
403 Forbidden           Authenticated but lacks permissions
404 Not Found           Resource does not exist
405 Method Not Allowed  Method not supported (check Allow header)
409 Conflict            Resource conflict (duplicate key, edit lock)
410 Gone                Permanently deleted; search engines purge
413 Payload Too Large   Request body exceeds server limits
415 Unsupported Media   Wrong Content-Type or encoding
422 Unprocessable       Valid syntax, semantic validation failure
429 Too Many Requests   Rate limited (check Retry-After header)

## 5xx Server Error
500 Internal Error      Unexpected server error (check server logs)
501 Not Implemented     Server does not support this method
502 Bad Gateway         Upstream service / backend crashed or invalid
503 Unavailable         Server overloaded or under maintenance
504 Gateway Timeout     Upstream service timed out

## Key Gotchas
- 401 vs 403: 401 = Missing/bad credentials. 403 = Credentials known, forbidden.
- 301/302 vs 307/308: 307 & 308 strictly preserve POST/PUT method & payload.
- 400 vs 422: 400 = Malformed JSON/syntax. 422 = Valid JSON, invalid field values.
