# Raspberry Pi WebSocket
WebSocket enables bidirectional communication in real time over the web.

WebSocket can be run together with a normal HTTP server. You can click a button in a web browser, and enable a GPIO on your Raspberry Pi which turns on a light in your house. All in real time, and with communication going both ways!

## Getting started with WebSockets in Tornado
### Getting started

Create a file named ```chat.py``` with this starter code:

```python
import tornado.ioloop
import tornado.web
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
 
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
 
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

You can run this server with `python3 chat.py`. If you navigate to `http://localhost:8888`, it should give an internal server error, since we haven’t written the `index.html` page yet.

###  Writing the index.html page

Let’s define a WebSocket with the following specification. It will be located at the route `/websocket` (that is, `http://localhost:8888/websocket`), and it takes a JSON dictionary with two key-value pairs: one key will be message, and the other key will be user. It sends a JSON dictionary to clients with the same format.

For example, we might make a request by sending the following dictionary to `/websocket`:

```shell
{
    “message”: “Hello world!”,
    “user”: “Neel”
}
```

hen we’ll make the page prompt the user to give a username on load. When a user sends a message, we’ll send the name that they enter as the value for “user”, and their message as the value for “message.” When the user receives a message, we’ll append it to a `div` on the page. Here’s some quick-and-dirty sample HTML (which we’ll save as `index.html`) that gets the job done:

```html 
<!DOCTYPE html>
<html>
<head>
    <title>Chat application</title>
</head>
<body>
    <div style="width:100%; padding: 20px; overflow-y: scroll;">
    <div id="messages"></div>
    <div style="padding-top: 20px;">
        <form onsubmit="return sendMessage()">
            <input id="message" type="text" style="width: 70%;"><button style="width: 25%">Send</button>
        </form>
    </div>
    <script>
    var ws = new WebSocket("ws://localhost:8888/websocket");
    var username = prompt("What's your name?");
 
    function sendMessage() {
        var messageInput = document.getElementById("message");
        var message = messageInput.value;
        var payload = {
            "message": message,
            "user": username
        }
        // Make the request to the WebSocket.
        ws.send(JSON.stringify(payload));
        // Clear the message from the input.
        messageInput.value = "";
        return false;
    }
 
    ws.onmessage = function(evt) {
        var messageDict = JSON.parse(evt.data);
        // Create a div with the format `user: message`.
        var messageBox = document.createElement("div");
        messageBox.innerHTML = messageDict.user + ": " + messageDict.message;
        document.getElementById("messages").appendChild(messageBox);
    };
    </script>
</body>
</html>
```

### Writing the WebSocket
Now, we’ll implement the `/websocket` route, by modifying the `chat.py` file accordingly:

```python
import tornado.ioloop
import tornado.web
import tornado.websocket
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
 
class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()
 
    def open(self):
        self.connections.add(self)
 
    def on_message(self, message):
        [client.write_message(message) for client in self.connections]
 
    def on_close(self):
        self.connections.remove(self)
 
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", SimpleWebSocket)
    ])
 
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```
And we’re done! You can run the server with python3 chat.py, and try out the chat box by opening http://localhost:8888 in multiple tabs.

