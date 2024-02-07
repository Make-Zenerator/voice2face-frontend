document.addEventListener('DOMContentLoaded', (event) => {
    // 공통된 내비게이션 핸들러
    function navigateTo(page) {
        window.location.href = page;
    }

    // 메인 페이지 이벤트 리스너
    document.getElementById('loginButton')?.addEventListener('click', () => {
        navigateTo('result.html'); // 로그인 페이지가 있다면 이동
    });

    // document.getElementById('createImage')?.addEventListener('click', () => {
    //     navigateTo('create.html');
    // });


    // 결과 페이지 이벤트 리스너
    document.getElementById('saveImage')?.addEventListener('click', () => {
        // 이미지 저장 로직
    });

    // main.html로 돌아가기

    document.getElementById('backToMain')?.addEventListener('click', () => {
        window.location.replace("main.html"); // 'main.html'로 이동하도록 수정
    });
});
