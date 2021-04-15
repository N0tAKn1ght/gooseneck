var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

var pgp = require('pg-promise')();

const dbConfig = {
    host: "ec2-54-167-152-185.compute-1.amazonaws.com",
    port: "5432",
    database: "d4a3mdi3t849lu",
    user: "qpeynpgjkccpxh",
    password: "f96f5d86cf1892bac455d2d0f1ea6fd71970ffbd8637a37e384150f4a74fa839"
}

var db = pgp(dbConfig);

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/'));

//connect to a website
app.get('/printCards', function(req,res){
    var name = 'SELECT name FROM images';
    var img = 'SELECT url from images';

    db.task('get-everything', task => {
        return task.batch([
            task.any(name),
            task.any(img)
        ]);
    })
    .then(item =>{
        console.log(item[1])
        res.render('pages/printCards', {
            my_title: "Card info",
            cardname: item[0],
            cardimg: item[1]
        })
    })
    .catch(error =>{
        res.render('pages/printCards', {
            my_title:"Error",
            cardname: '',
            cardimg: ''
        })
    })
});


app.listen(3000);
console.log('Should print all database');