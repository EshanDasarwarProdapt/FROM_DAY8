const products = require('./product.json')

console.log('\nActivity1 -Display Products Nmaes')

products.forEach(product=>{
    console.log(`${product.name} - ₹${product.price}`)
    //return(f"{variablevalue} display)
})

console.log('\nActivity2 - Calculate Total Price')

const totalPrice = products.map(product => ({
    name: product.name,
    totalPrice: product.price * product.quantity
}));

console.log(totalPrice);

console.log('\nActivity3 - Find Available Products')

const availableProducts = products.filter(product=>product.inStock)
console.log(availableProducts)