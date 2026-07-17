import { getBookings } from "./api/getBookings.js";

async function main(){
    console.log("Fetching latest bookings from json server...\n")
    const bookings = await getBookings();
    console.table(bookings)
}
main();