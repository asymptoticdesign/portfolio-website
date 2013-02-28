var interval;
var width, height;
var canvas, ctx;
var noiseScale = 0.002;
var particleList = new Array();
var numParticles = 200;

function setup() {
    width = 800;
    height = 300;
    perlin = new SimplexNoise();
    canvas = document.getElementById("demo");
    ctx = canvas.getContext("2d");
    ctx.fillStyle = "rgb(255,255,255)";
    ctx.fillRect(0,0,width,height);
    interval = setInterval(draw,50);
    for(i = 0; i < numParticles; i++) {
	particleList[i] = new Particle();
    }
}
    
function draw() {
    for(i = 0; i < numParticles; i++) {
	particleList[i].update();
	particleList[i].render();
    }
}

function Particle() {
    this.x = width*Math.random();
    this.y = height*Math.random();
    this.rad = 1;

    this.update = function() {
	//update the x and y based on perlin noise
	this.x += 0.5*Math.sin(2*Math.PI*perlin.noise(noiseScale*this.x,noiseScale*this.y));
	this.y += 0.5*Math.cos(2*Math.PI*perlin.noise(noiseScale*this.x,noiseScale*this.y));
	//deal with edge cases to wrap around
	if (this.x < 0) {
	    this.x = width;
	}
	if (this.x > width) {
	    this.x = 0;
	}
	if (this.y < 0) {
	    this.y = height;
	}
	if (this.y > height) {
	    this.y = 0;
	}
    }

    this.render = function() {
	ctx.beginPath();
	ctx.fillStyle = "rgba(0,0,0,0.1)"
	ctx.arc(this.x,this.y,this.rad,0,2*Math.PI,true);
	ctx.fill();
    }
}