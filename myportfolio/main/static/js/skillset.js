document.getElementById("left_button").addEventListener("click",moveLeft)
document.getElementById("right_button").addEventListener("click",moveRight)
function moveLeft() {
    const introScreens = ["intro_1", "intro_2", "intro_3", "intro_4", "intro_5", "intro_6"];
    let currentIndex = -1;

    // 현재 화면 찾기
    for (let i = 0; i < introScreens.length; i++) {
        if (window.getComputedStyle(document.getElementById(introScreens[i])).opacity === "1") {
            currentIndex = i;
            break;
        }
    }

    if (currentIndex !== -1) {
        const prevIndex = (currentIndex - 1 + introScreens.length) % introScreens.length; // 이전 화면 인덱스 계산

        // 현재 화면을 숨기고 이전 화면을 표시
        document.getElementById(introScreens[currentIndex]).style.opacity = "0";
        document.getElementById(introScreens[currentIndex]).style.display = "none";

        document.getElementById(introScreens[prevIndex]).style.opacity = "1";
        document.getElementById(introScreens[prevIndex]).style.display = "block";
    }
}

function moveRight() {
    const introScreens = ["intro_1", "intro_2", "intro_3", "intro_4", "intro_5", "intro_6"];
    let currentIndex = -1;

    // 현재 화면 찾기
    for (let i = 0; i < introScreens.length; i++) {
        if (window.getComputedStyle(document.getElementById(introScreens[i])).opacity === "1") {
            currentIndex = i;
            break;
        }
    }

    if (currentIndex !== -1) {
        const nextIndex = (currentIndex + 1) % introScreens.length; // 다음 화면 인덱스 계산

        // 현재 화면을 숨기고 다음 화면을 표시
        document.getElementById(introScreens[currentIndex]).style.opacity = "0";
        document.getElementById(introScreens[currentIndex]).style.display = "none";

        document.getElementById(introScreens[nextIndex]).style.opacity = "1";
        document.getElementById(introScreens[nextIndex]).style.display = "block";
    }
}




// Matter.js의 모듈을 변수에 할당
const { Engine, Render, Runner, World, Bodies, Mouse, MouseConstraint, Body } = Matter;

// 엔진 생성
const engine = Engine.create();
const { world } = engine;

// 렌더링 설정
const web_canvas=document.getElementById('canvasContainer')
const render = Render.create({
    element: canvasContainer,
    engine: engine,
    options: {
        background: 'white',
        width: 800,
        height: 600,
        wireframes: false
    }
});

//구조물 생성 (reset)
// 바닥 생성
function start_engine(){
    const ground = Bodies.rectangle(2400, 610, 4810, 21, { 
        isStatic: true, 
        render: { 
            fillStyle: 'white' 
        } 
    });
    // 벽 생성
    const wall1 = Bodies.rectangle(-10, 0, 10, 2600, { 
        isStatic: true, 
        render: { 
            fillStyle: 'white' 
        } 
    });

    const wall2 = Bodies.rectangle(803, 0, 10, 2600, { 
        isStatic: true, 
        render: { 
            fillStyle: 'white' 
        } 
    });

    World.add(world, ground);
    World.add(world, wall1);
    World.add(world, wall2);
}

start_engine()

// 렌더링 시작
Render.run(render);
const runner = Runner.create();
Runner.run(runner, engine);

// 마우스 조작 추가
const mouse = Mouse.create(render.canvas);
const mouseConstraint = MouseConstraint.create(engine, {
    mouse: mouse
});
World.add(world, mouseConstraint);
render.mouse = mouse;


// 버튼을 누르면 랜덤한속도로 포물선 발사하기위한 랜덤숫자 fx()
function generateRandomX() {
    return Math.floor(Math.random() * 15); // 랜덤 숫자 반환
}

function generateRandomY() {
    // Math.random()은 0부터 1미만의 숫자를 반환하므로, -5부터 -15까지를 얻으려면
    // 먼저 0부터 -10까지의 랜덤한 숫자를 얻고 거기에 -5를 더합니다.
    return Math.floor(Math.random() * 11) - 15;
}

//random 하게 하늘에서 떨어지게 하기위한 0~800좌표
function randomsky() {
    return (Math.random() * 800);
}
// random한 높이에서 떨어지게 하기 위한 0~-100 좌표
function upSky() {
    return (Math.random() * -1000);
}

// 종이 떨어지는 방향 느낌 자유롭게 ==> 잘 적용 안되는 것 같음 다른 방법 찾아보기
function paperXVec() {
    return (Math.random() * 50 -25)
}

//별 랜덤색상
function starColor() {
    const colors = ['#00FF00', '#FFD700', '#FFFF00', '#FFA500', '#FF00FF', '#4B0082', '#FFFFE0', '#FFFACD'];
    return colors[Math.floor(Math.random() * colors.length)];
}

// 랜덤 각도
function generateRandomR() {
    return (Math.random() * 2 - 1);
}

// base random 색상
function getRandomColor() {
    const colors = ['red', 'blue', '#0000FF', 'yellow', 'green', '#F5F5DC', 'black', 'pink'];
    const goldChance = 0.02;  // 황금색이 나올 확률
    const randomNum = Math.random();  // 0과 1 사이의 랜덤한 숫자를 생성

    if (randomNum < goldChance) {
        return 'gold';  // 황금색이 선택됨
    }

    const randomIndex = Math.floor(Math.random() * colors.length);
    return colors[randomIndex];  // 랜덤한 색상이 선택됨
}

//신발윗부분 색상
function getRandomShoeCover() {
    const colors = ['#F0F8FF','	#F5FFFA','#F8F8FF','#FFFFF0','white']
    return colors[Math.floor(Math.random() * colors.length)];
}



/* 버튼들 관련 함수 */

document.querySelector('.btn-html').addEventListener('click', function() {
    // 빨간색 벽돌을 생성하는 코드 (예시)
    const box = Bodies.rectangle(20, 200, 20, 40, { 
        render: {
            fillStyle: 'red',
            strokeStyle: '#800000',  // 태두리 색
            lineWidth: 3  // 태두리 두께
        }
    });
    Matter.Body.setVelocity(box, { x: generateRandomX(), y: generateRandomY() });
    Matter.Body.setAngularVelocity(box, generateRandomR());
    World.add(world, box);
});



//css 완성
document.querySelector('.btn-css').addEventListener('click', function() {
    const base_color = getRandomColor()
    const tong = '	#E6E6FA'
    const rectangle1 = Bodies.rectangle(0, 0, 60, 40,{
        render: {
            fillStyle: base_color
            }
        });
    
    let ellipseVertices = [];
    const numVertices = 30;  // 꼭짓점 수
    const a = 30;  // 가로 반지름
    const b = 5;  // 세로 반지름
    const x = 0;  // 중심의 x 좌표
    const y = 20;  // 중심의 y 좌표
    
    for(let i = 0; i < numVertices; i++) {
        const angle = Math.PI * 2 * (i / numVertices);
        const xPos = x + a * Math.cos(angle);
        const yPos = y + b * Math.sin(angle);
        ellipseVertices.push({ x: xPos, y: yPos });
    }
    
    const circle1 = Bodies.fromVertices(x, y, [ellipseVertices], {
        render: {
            fillStyle: '#DCDCDC',
            strokeStyle: 'black',
            lineWidth: 0.1
        }
    });

    const rectangle2 = Bodies.rectangle(0,-40,60,40,{
        render: {
            fillStyle: tong
            }
        });

    
    let ellipseVertices2 = [];
    const x2 = 0;  // 중심의 x 좌표
    const y2 = -20;  // 중심의 y 좌표
    
    for(let i = 0; i < numVertices; i++) {
        const angle = Math.PI * 2 * (i / numVertices);
        const xPos = x2 + a * Math.cos(angle);
        const yPos = y2 + b * Math.sin(angle);
        ellipseVertices2.push({ x: xPos, y: yPos });
    }
    
    const circle2 = Bodies.fromVertices(x2, y2, [ellipseVertices2], {
        render: {
            fillStyle: base_color
        }
    });

    let ellipseVertices3 = [];
    const x3 = 0;  // 중심의 x 좌표
    const y3 = -60;  // 중심의 y 좌표
    
    for(let i = 0; i < numVertices; i++) {
        const angle = Math.PI * 2 * (i / numVertices);
        const xPos = x3 + a * Math.cos(angle);
        const yPos = y3 + b * Math.sin(angle);
        ellipseVertices3.push({ x: xPos, y: yPos });
    }
    
    const circle3 = Bodies.fromVertices(x3, y3, [ellipseVertices3], {
        render: {
            fillStyle: tong
        }
    });




    
    
    
    const compoundBody = Body.create({
        parts: [rectangle1, circle1,rectangle2, circle2, circle3]
    });
    // 도형의 초기 위치 설정
    Body.setPosition(compoundBody, { x: 170, y: 200 });
    // 도형의 초기 속도 설정
    Body.setVelocity(compoundBody, { x: generateRandomX(), y: generateRandomY() });
    Body.setAngularVelocity(compoundBody, generateRandomR())
    // 복합 도형을 세계에 추가
    World.add(world, [compoundBody]);
});

// javascript 마무리!
document.querySelector('.btn-javascript').addEventListener('click', function() {
    for (let i = 0; i < 30; i++) {  // 5번 반복하여 별 생성
        const sky = randomsky();
        const upsky = upSky();
        const starcolor = starColor();
        const star = Bodies.polygon(100, 0, 5, 4, {
            render: {
                strokeStyle: starcolor,
                lineWidth: 1
            }
        });
        
        Matter.Body.setPosition(star, { x: sky, y: upsky });
        World.add(world, star);
    }
});



//장고
document.querySelector('.btn-django').addEventListener('click', function() {
    // 신발의 '뒷굽' 부분을 원으로 생성
    const CD = Bodies.circle(0, 0, 25);

    // 신발의 '앞코' 부분을 원으로 생성
    const hole = Bodies.circle(0, 0, 5,{
        render: {
            fillStyle:'white'
        }
    });

    // 복합 도형으로 신발 생성
    const shoe = Body.create({
        parts: [CD, hole]
    });

    // 도형의 초기 위치 설정
    Body.setPosition(shoe, { x: 200, y: 200 });

    // 도형의 초기 속도 설정
    Body.setVelocity(shoe, { x: generateRandomX(), y: generateRandomY() });
    Body.setAngularVelocity(shoe, generateRandomR());

    // 복합 도형을 세계에 추가
    World.add(world, [shoe]);
});





// bootstrap
document.querySelector('.btn-bootstrap').addEventListener('click', function() {
    for (let i = 0; i < 30; i++) {  // 5번 반복하여 별 생성
        const sky = randomsky();
        const upsky = upSky();
        const paperX = paperXVec();
        const paper = Bodies.rectangle(100, 0, 8, 8, {
            density: 0.001,          // 높은 밀도로 설정 (선택적)
            frictionAir: Math.random()         // 공기 저항 값 설정
        });
        
        Matter.Body.setPosition(paper, { x: sky, y: upsky });
        Matter.Body.setVelocity(paper, { x: paperX, y:0})
        World.add(world, paper);
    }

});

/* beautifulsoup 끝끝끝끝 */ 
document.querySelector('.btn-beautifulsoup').addEventListener('click', function() {
    const base_color = getRandomColor()
    const shoeCover = getRandomShoeCover()
    // 원과 사각형을 생성
    const circle = Bodies.circle(0, 0, 15);
    const rectangle = Bodies.rectangle(20, 0, 40, 30,{
        render: {
            fillStyle: base_color
        }
    });
    const rectangle2 = Bodies.rectangle(54,25,30,80,{
        render: {
            fillStyle: base_color
        }
    });
    
    //삼각형
    const vertices = [
        { x: 40, y: 65 },
        { x: 40, y: 15 },
        { x: 0, y: 15 },
      ];
      
    const triangle = Bodies.fromVertices(26, 32, vertices,{
        render: {
            fillStyle: 	shoeCover
        }
    });

    //신발끈
    const shoelace1 = Bodies.rectangle(13,22,3,12,{
        render: {
            fillStyle: 'black'
        }
    })
    const lace1R = Math.PI / 180 * 49;
    Body.rotate(shoelace1, lace1R);

    //신발끈2
    const shoelace2 = Bodies.rectangle(19,30,3,12,{
        render: {
            fillStyle: 'black'
        }
    })
    const lace2R = Math.PI / 180 * 49;
    Body.rotate(shoelace2, lace2R);
    //신발끈3
    const shoelace3 = Bodies.rectangle(25,38,3,12,{
        render: {
            fillStyle: 'black'
        }
    })
    const lace3R = Math.PI / 180 * 49;
    Body.rotate(shoelace3, lace3R);

    //여기부터 오각형만들기
    const pentagon = Bodies.polygon(50, 0, 5, 12, {
        render: {
          strokeStyle: 'black',
          lineWidth: 1
        }
      });
    const angleInRadians = Math.PI / 180 * -17;
    Body.rotate(pentagon, angleInRadians);

    // 복합 도형을 생성
    const compoundBody = Body.create({
        parts: [circle, rectangle,rectangle2,pentagon,triangle, shoelace1, shoelace2, shoelace3]
    });
    // 도형의 초기 위치 설정
    Body.setPosition(compoundBody, { x: 170, y: 200 });
    // 도형의 초기 속도 설정
    Body.setVelocity(compoundBody, { x: generateRandomX(), y: generateRandomY() });
    Body.setAngularVelocity(compoundBody, generateRandomR())
    // 복합 도형을 세계에 추가
    World.add(world, [compoundBody]);
});

// selenium
document.querySelector('.btn-selenium').addEventListener('click', function() {
    Matter.World.remove(engine.world, engine.world.bodies);
    start_engine()
});

/* AI 부분 canvas */

const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
const slider = document.getElementById('slider');
const output = document.getElementById("sliderValue");
let painting = false;


output.value = slider.value;

slider.oninput = function() {
    output.value = this.value;
}



function startPosition(e) {
    painting = true;
    draw(e);
}
function endPosition() {
    painting = false;
    ctx.beginPath();
}

function draw(e) {
    if (!painting) return;
    let pickColor = document.getElementById('colorpicker').value
    let lineWidth = document.getElementById('slider').value;

    ctx.strokeStyle = pickColor;
    ctx.lineWidth = lineWidth;
    ctx.lineCap = "round";
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  }



document.getElementById("pen").addEventListener("click", setPen);
document.getElementById("eraser").addEventListener("click", setEraser);

function setPen(){
    ctx.globalCompositeOperation = 'source-over';
    document.getElementById("penImg").style.width="20px";
    document.getElementById("eraserImg").style.width="15px";
}
function setEraser(){
    ctx.globalCompositeOperation = 'destination-out';
    document.getElementById("penImg").style.width="15px";
    document.getElementById("eraserImg").style.width="20px";
}

canvas.addEventListener("mousedown", startPosition);
canvas.addEventListener("mouseup", endPosition);
canvas.addEventListener("mousemove", draw);


document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("artForm");
    const canvas = document.getElementById("myCanvas");
    const hiddenInput = document.getElementById("myCanvasData");

    form.addEventListener("submit", function(event) {
        const title = document.getElementById("title").value;
        const artist = document.getElementById("artist").value;

        if (!title) {
            alert("제목을 입력해주세요.");
            event.preventDefault();
            return;
        }

        if (!artist) {
            alert("이름을 입력해주세요.");
            event.preventDefault();
            return;
        }

        // Canvas의 데이터를 Base64 형식으로 추출
        const canvasData = canvas.toDataURL();
        hiddenInput.value = canvasData;  // 숨겨진 input 필드에 canvas 데이터 저장
    });
});

TypeHangul.type('#fixed_content',{
    intervalType: 5
});