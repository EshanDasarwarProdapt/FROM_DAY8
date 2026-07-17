const BASE_URL = "http://localhost:3000/booking";
export async function updateBooking(id,booking)
{
    const response = await fetch("http://localhost:3000/bookings",{
        method : "PUT",
        headers:{
            "Content-Type" : "application/json"
        },

        body : JSON.stringify(booking)
    });
    // return await response.json();
    if(!response.ok)
    {
        console.log("Error fetching the api ")
    }
const bookig = await response.json()
console.log("Booking Update successfuly")
return booking


}