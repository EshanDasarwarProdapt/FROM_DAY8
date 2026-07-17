export async function addBooking(booking){

    const response = await fetch("http://localhost:3000/bookings", {
        
        method: "POST",
    
    headers:{
        "Content-Type": "application/json"
    },
    body: JSON.stringify(booking)

});

    return await response.json();
}