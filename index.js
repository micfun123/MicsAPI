const app = require('express')();
const PORT = 3000;

app.listen(
    PORT,
    () => console.log(`Server is running on port http://localhost:${PORT}`)
);

app.get('/', (req, res) => {
    res.send('Hello World!');
});

//name response

app.get('/random_dog_image', (req, res) => {
    //random number between 1 and 100
    let randomint = Math.floor(Math.random() * 5) + 1;
    //send a respomce in json format 
    res.json({
        image: `https://placedog.net/500/280?id=${randomint}`
    });

});
