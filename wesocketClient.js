const socket = new WebSocket("ws://localhost:8000/ws");

socket.onopen = () => {
  console.log("WebSocket connection established");
  socket.send("Hello, server!");
};

socket.onmessage = (event) => {
  console.log("Received message from server:", event.data);
};

socket.onclose = () => {
  console.log("WebSocket connection closed");
};
