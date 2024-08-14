<script>
  import ButtonStyleOutlined from "../join/ButtonStyleOutlined.svelte";
  import Header from "../../components/header/header_login.svelte";

  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';

  const loadingImage = "./_src_temp/loading_image.png";

  let isLoggedIn = false;
  let checkedSession = false; // 세션 체크가 완료되었는지 확인하는 변수

  function checkSession() {
    console.log('세션 토큰 확인 중...');
    const token = sessionStorage.getItem('auth_token');
    console.log('토큰:', token);
    if (!token) {
      alert(`세션이 만료되었습니다.\n다시 로그인 해주세요.`);
      goto('/login');
    } else {
      isLoggedIn = true;
    }
    checkedSession = true; // 세션 체크 완료
  }

  onMount(() => {
    checkSession();
  });
</script>

<style>
  .frame { /* 전체 프레임 영역*/ 
    align-items: center;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    position: relative;
  }

  .main-container { /* 디자인 영역 */
    top: 180px;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 82px;
    padding: 0px 0px 60px 0px;
    position: relative;
    width: 1200px;
    margin-bottom: 60px;
  }

  .inner-container {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 1103px;
    height: 429px;
    position: relative;
  }

  .card-container {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    height: 423px;
    position: relative;
  }

  .card {
    background: #ffffff;
    border-radius: 10px;
    border-style: solid;
    border-color: #878787;
    border-width: 0.5px;
    padding: 20px; /* Adjusted padding */
    display: flex;
    flex-direction: column; /* Changed to column */
    gap: 20px; /* Adjusted gap */
    align-items: center; /* Centered alignment */
    justify-content: center;
    flex-shrink: 0;
    width: 451px; /* Increased width */
    height: 395px; /* Auto height to fit content */
    position: relative;
    box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
    overflow: hidden;
  }

  .loading-header {
    color: #000000;
    text-align: center;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 46px;
    line-height: 1.2; /* Adjusted line height */
    font-weight: 700;
    width: 100%;
    margin-bottom: 20px; /* Added margin */
  }

  .content {
    display: flex;
    flex-direction: column;
    gap: 40px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    height: auto; 
    width: 100%;
    position: relative;
  }

  .text-container {
    display: flex; 
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
  }

  .text {
    text-align: center;
    font-size: 16pt;
    width: 100%;
    color: #6b6b6b ;
  }

  .button {
    border-color: var(--7b95b7, #6b6b6b);
    flex-shrink: 0;
    height: 46px;
  }

  .placeholder {
    flex-shrink: 0;
    width: 400.99px;
    height: 400.99px;
    border-radius: 24px; 
    padding: 10px; 
    display: flex; 
    flex-direction: row; 
    gap: 10px; 
    align-items: center; 
    justify-content: center; 
    align-self: stretch; 
    flex: 1; 
    position: relative; 
    overflow: visible;
  }

  @media (max-width: 420px) {
    .main-container {
      top: 255.5px;
      width: 100%;
      padding: 0px 16px 40px 16px;
      align-items: center;
      gap: 40px;
      margin-bottom: 30px;
    }

    .inner-container {
      flex-direction: column;
      gap: 40px;
      width: 100%;
      align-items: center;
      justify-content: center;
    }

    .card-container {
      flex-direction: column;
      gap: 20px;
      width: 100%;
      align-items: center;
      justify-content: center;
    }

    .card {
      width: 100%;
      height: auto;
      padding: 40px 20px 40px 20px;
    }

    .loading-header {
      font-size: 32px;
      line-height: 1.4;
    }

    .text {
      font-size: 14pt;
    }

    .placeholder {
      width: 100%;
      height: auto;
      max-width: 400px;
    }
  }
</style>

<div class="frame">
  {#if checkedSession && isLoggedIn}
    <div class="main-container">
      <Header />
      <div class="inner-container">
        <div class="card-container">
          <div class="card">
            <div class="content">
              <div class="text-container">
                <div class="loading-header">로딩 중 이에요...</div>
                <div class="text">
                  생성 요청했습니다. <br />
                  완료되면 화면이 자동으로 변환됩니다.
                </div>
              </div>
              <ButtonStyleOutlined
                class="button"
                name="메인으로 돌아가기"
                targetPath="/home"
              ></ButtonStyleOutlined>
            </div>
          </div>
          <img
            class="placeholder"
            src={loadingImage}
            alt="login_image"
          />
        </div>
      </div>
    </div>
  {/if}
</div>
