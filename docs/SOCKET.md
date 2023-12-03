# Socket module

## What is it?

Socket module is a part of the backend responsible for handling socket connections. It is used to communicate with the frontend and to send notifications to the user.

## How does it work?

Socket module is a simple socket server that listens on port 3000. It is implemented using the [socket.io](https://socket.io/) library. It is used to send notifications to the user when the AI module finishes processing the data. It is also used to send notifications to the user when the user is connected to the socket server and the AI module finishes processing the data.

## How to use it?

### Sending notifications to the user

To send a notification to the user, you need to emit a `<event_name>` event to the socket server.

## Events

### after connect

This event is emitted by the socket server when the user connects to the socket server. It is used to send notifications to the user when the user is connected to the socket server.

### after disconnect

This event is emitted by the socket server when the user disconnects from the socket server.

### analyse

This event is emitted by user when the user wants to start the analysis.

### progress

This event is emitted by the socket server as a status update.

### done

This event is emitted by the socket server when the analysis is done.

### failed

This event is emitted by the socket server when the analysis fails.