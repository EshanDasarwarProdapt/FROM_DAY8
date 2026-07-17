const products = require('./product.json');

console.log('\nActivity1 - Display Products Names');

products.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`);
});


console.log('\nActivity2 - Calculate Total Price');

const totalPrice = products.map(product => ({
    name: product.name,
    totalPrice: product.price * product.quantity
}));

console.log(totalPrice);


console.log('\nActivity3 - Find Available Products');

const availableProducts = products.filter(product => product.inStock);
console.log(availableProducts);


console.log('\nActivity4 - Find Expensive Product');

const ExpensiveProduct = products.filter(product => product.price > 5000);
console.log(ExpensiveProduct);


console.log('\nActivity5 - Search Product');

const SearchProduct = products.find(product => product.id === 103);
console.log(SearchProduct);


console.log('\nActivity6 - Check Availability');

const checkAvailability = products.some(product => !product.inStock);
console.log(checkAvailability);


console.log('\nActivity7 - Verify Stock Status');

const CheckStock = products.every(product => product.inStock);
console.log(CheckStock);


console.log('\nActivity8 - GrandTotal');

const GrandTotal = products.reduce((total, product) => {
    return total + (product.price * product.quantity);
}, 0);

console.log(GrandTotal);


console.log('\nActivity9 - Sort Products');

const SortProduct = [...products].sort((a, b) => a.price - b.price);

SortProduct.forEach(product => {
    console.log(product.name);
});


console.log('\nActivity10 - Display only Product Name');

const displayProduct = products.map(product => product.name);
console.log(displayProduct);


console.log('\nActivity11 - Find Product Position');

const index = products.findIndex(product => product.name === "Office Chair");
console.log(index);


console.log('\nActivity12 - Remove Out of stock');

const RemoveStock = products.filter(product => product.inStock);
console.log(RemoveStock);


console.log('\nActivity13 - GST');

const productWithGST = products.map(product => ({
    ...product,
    gst: product.price * 0.18
}));

console.log(productWithGST);


console.log('\nActivity14 - 3 Cheapest');

const CheapestProduct = [...products]
    .sort((a, b) => a.price - b.price)
    .slice(0, 3);

CheapestProduct.forEach(product => {
    console.log(`${product.name} - ₹${product.price}`);
});

console.log('\nActivity15 - Generate Bill Summary');

const BillSummary = products.reduce((summary, product) => {
    summary.totalProducts += 1;
    summary.totalQuantity += product.quantity;
    summary.totalAmount += product.price * product.quantity;

    return summary;
}, {
    totalProducts: 0,
    totalQuantity: 0,
    totalAmount: 0
});

console.log(BillSummary);