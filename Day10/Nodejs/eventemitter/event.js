import EventEmitter from "events"

const emitter = new EventEmitter();

emitter.on("greet",(name) => {
    console.log(`Hello ${name}`);
});

emitter.emit("greet","Rahul");