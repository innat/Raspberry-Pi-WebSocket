$(document).ready(function(){

        var WEBSOCKET_ROUTE = "/ws";

        if(window.location.protocol == "http:"){
            //localhost
            var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
            }
        else if(window.location.protocol == "https:"){
            //Dataplicity
            var ws = new WebSocket("wss://" + window.location.host + WEBSOCKET_ROUTE);
            }

        ws.onopen = function(evt) {
            $("#ws-status").html("Connected");
            };

        ws.onmessage = function(evt) {
            };

        ws.onclose = function(evt) {
            $("#ws-status").html("Disconnected");
            };

        $("#green_on").click(function(){
            ws.send("on_g");
            });

        $("#green_off").click(function(){
            ws.send("off_g");
            });

        $("#red_on").click(function(){
            ws.send("on_r");
            });

        $("#red_off").click(function(){
            ws.send("off_r");
            });

	$("#blue_on").click(function(){
            ws.send("on_b");
            });

        $("#blue_off").click(function(){
            ws.send("off_b");
            });

	$("#white_on").click(function(){
            ws.send("on_w");
            });

        $("#white_off").click(function(){
            ws.send("off_w");
            });


      });
