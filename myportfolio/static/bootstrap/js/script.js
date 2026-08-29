

$('.category').each(function() {
  $(this).find('li').click(function() {
    // 현재 클릭한 요소에 meanbtn 클래스가 있는지 확인
    if ($(this).hasClass('meanbtn')) {
      // meanbtn 클래스 제거하고 active 클래스 추가
      $(this).removeClass('meanbtn').addClass('active');
      $(this).siblings('.active').removeClass('active').addClass('meanbtn');
    } else {
      // 다른 요소에는 meanbtn 클래스 적용
      $(this).removeClass('meanbtn').addClass('active');
    }
  });
});

$('.rankCategory').each(function() {
  $(this).find('li').click(function() {
    // 현재 클릭한 요소에 meanbtn 클래스가 있는지 확인
    if ($(this).hasClass('meanbtn')) {
      // meanbtn 클래스 제거하고 active 클래스 추가
      $(this).removeClass('meanbtn').addClass('active');
      $(this).siblings('.active').removeClass('active').addClass('meanbtn');
    } else {
      // 다른 요소에는 meanbtn 클래스 적용
      $(this).removeClass('meanbtn').addClass('active');
    }
  });
});

var ascending = true; // 초기 정렬 순서 (오름차순)

$('.buttons').click(function() {
  var clickedBtn = $(this);

  ascending = !ascending; 

  if (ascending) {
    clickedBtn.removeClass('borderTop').addClass('borderBottom');
    $('.buttons').not(clickedBtn).removeClass('borderTop borderBottom');
  } else {
    clickedBtn.removeClass('borderBottom').addClass('borderTop')
    $('.buttons').not(clickedBtn).removeClass('borderTop borderBottom');
  }

});


$(document).ready(function() {
  $('.accordion_win_btn').click(function() {
    var accordionContent = $(this).closest('.my-custom-accordion').find('.accordion-content');
    if (accordionContent.hasClass('accordion_active')) {
      accordionContent.slideUp(500, 'swing' ).removeClass('accordion_active');
    } else {
      accordionContent.slideDown(800, 'swing' ).addClass('accordion_active');
    }
  });
});
$(document).ready(function() {
  $('.accordion_lose_btn').click(function() {
    var accordionContent = $(this).closest('.my-custom-accordion').find('.accordion-content');
    if (accordionContent.hasClass('accordion_active')) {
      accordionContent.slideUp(500, 'swing' ).removeClass('accordion_active');
    } else {
      accordionContent.slideDown(800, 'swing' ).addClass('accordion_active');
    }
  });
});



//  보여지는 통계부분 



{/* <ul class="nav" style="width: 1080px;height: 40px; background-color:#fff; align-items: center; margin-top: 2px;" >
<li style="width: 4%;height: 40px; margin-left: -5px;">
    <P class="pitems">1</P>
</li>
<li style="width: 11%;height: 40px; display: flex;">
    <img class="meanchamp" src ='{% static "images/ez.png" %}' alt="이즈">
    <P class="pitems" style="margin-left: -10px;">이즈리얼</P>
</li>
<li style="width: 11%;height: 40px;">
    <P class="pitems fw-bolder rank sort">4,833,847</P>
</li>
<li style="width: 8%;height: 40px;">
    <P class="pitems">2.42:1</P>
</li>
<li class="d-flex" style="width: 15%;height: 40px; margin-right: 10px;">
    <progress id="progress" value="49.29" min="0" max="100" ></progress>
    <P class="pitems">49.29%</P>
</li>
<li class="d-flex" style="width: 15%;height: 40px; margin-right: -10px;">
    <progress id="progress" value="23" min="0" max="100" ></progress>
    <P class="pitems">23%</P>
</li>
<li style="width: 11%;height: 40px;">
    <P class="pitems">8.31%</P>
</li>
<li style="width: 9%;height: 40px;">
    <P class="pitems">183.79</P>
</li>
<li style="width: 7%;height: 40px;">
    <P class="pitems">10902</P>
</li>
<li style="width: 7%;height: 40px;">
    <P class="pitems">58%</P>
</li>
</ul> */}
