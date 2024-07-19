<script>
  import BasicFilled from "../../components/button/basic_filled.svelte";
  import PlaceholderImage from "./PlaceholderImage.svelte";
  import Header from "../../components/header/header_non.svelte";
  import { goto } from '$app/navigation';

  const serverIP = import.meta.env.VITE_SERVER_IP;

  let className = "";
  export { className as class };
  export let style;
  let login_email;
  let login_pswd;
  let targetPath = "/home";

  async function login() {
    const formData = new FormData();
    formData.append('email', login_email);
    formData.append('password', login_pswd);

    try {
      const response = await fetch(`${serverIP}/api/v1/auth`, {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json(); // 백엔드로부터 받은 데이터를 JSON으로 파싱
        const { token, email } = data; // 파싱된 JSON 객체에서 token과 email을 추출

        // 토큰과 이메일을 로컬 스토리지에 저장
        sessionStorage.setItem('auth_token', token);

        alert(`로그인 성공!`);

        goto(targetPath); // 사용자를 홈 페이지로 리다이렉트
      } else {
        alert('로그인 실패 \n 이메일과 비밀번호를 확인해주세요');
        console.log(response);
      }
    } catch (error) {
      console.error('로그인 중 에러 발생:', error);
      alert('로그인 중 에러가 발생했습니다.');
    }
  }
</script>

<style>
  form {
    background: var(--neutral-0, #ffffff);
    display: flex;
    flex-direction: column;
    gap: 120px;
    align-items: center;
    justify-content: flex-start;
    position: relative;
  }

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
    gap: 160px;
    padding: 0px 0px 120px 0px;
    position: relative;
    width:1200px;
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

  .login-wrapper {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    height: 423px;
    position: relative;
  }

  .login-container {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    height: 401px;
    position: relative;
  }

  .login-box {
    background: #ffffff;
    border-radius: 10px;
    border-style: solid;
    border-color: #878787;
    border-width: 0.5px;
    padding: 47px 0px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 451px;
    height: 395px;
    position: relative;
    box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
    overflow: hidden;
  }

  .login-content {
    top: -13px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .login-header {
    color: #000000;
    text-align: center;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 46px;
    line-height: 40px;
    font-weight: 700;
    position: relative;
    width: 451px;
    height: 40px;
  }

  .input-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .input-label {
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 19px;
    line-height: 40px;
    font-weight: 500;
    position: relative;
    width: 125px;
    height: 23px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }

  .input-box {
    background: #ffffff;
    border-radius: 10px;
    border-style: solid;
    border-color: #000000;
    border-width: 1px;
    padding: 1px 43px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 337px;
    position: relative;
    overflow: hidden;
  }

  .input {
    color: rgba(0, 0, 0, 0.4);
    text-align: center;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 18px;
    line-height: 30px;
    font-weight: 500;
    position: relative;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    background: transparent;
    -webkit-appearance: none;
  }

  .login-button {
    background: var(--7b95b7, #6b6b6b);
    flex-shrink: 0;
  }

  .img-box{
    border-radius: 24px;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 405px;
    height: 405px;
    position: relative;
    overflow: visible;
  }

  /* .placeholder {
    flex-shrink: 0;
    width: 405px;
    height: 405px;
  } */

  @media(max-width: 1120px) {
  .login-container {
    flex-direction: column;
  }
  
  .img-box{
    width: 401px;
    height: 401px;
  }
}


  @media(max-width: 420px) {
  form {
    gap: 60px;
  }

  .frame {
    padding: 0 16px;
  }

  .main-container {
    top: 120px;
    width: 100%;
    padding: 0;
    gap: 80px;
    align-items: center;
  }

  .inner-container {
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
  }

  .login-wrapper {
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
  }

  .login-container {
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
  }

  .login-box {
    width: 100%;
    padding: 50px 20px 0px 20px;
    box-sizing: border-box;
  }

  .login-content {
    width: 100%;
    gap: 20px;
  }

  .login-header {
    font-size: 32px;
    line-height: 36px;
    width: 100%;
  }

  .input-group {
    width: 100%;
    gap: 10px;
  }

  .input-label {
    font-size: 16px;
    line-height: 20px;
    width: 100%;
  }

  .input-box {
    width: 100%;
  }

  .input {
    font-size: 16px;
    line-height: 24px;
  }

  .login-button {
    width: 100%;
  }

  .img-box{
    width: 100%;
    max-width: 300px;
    height: auto;
  }
}

</style>

<form on:submit|preventDefault={login} class="form-container" style={style}>
  <div class="frame">
    <div class="main-container">
      <Header />
      <div class="inner-container">
        <div class="login-wrapper">
          <div class="login-container">
            <div class="login-box">
              <div class="login-content">
                <div class="login-header">로그인</div>
                <div class="input-group">
                  <div class="input-label">이메일 주소</div>
                  <div class="input-box">
                    <input type='email' bind:value={login_email} placeholder="이메일 입력" class="input" />
                  </div>
                </div>
                <div class="input-group">
                  <div class="input-label">비밀번호</div>
                  <div class="input-box">
                    <input type='password' bind:value={login_pswd} placeholder="비밀번호 입력" class="input" />
                  </div>
                </div>
                <BasicFilled
                  styleVariant="filled"
                  style=
                  " top: 10px;
                    background: var(--7b95b7, #6b6b6b);
                    flex-shrink: 0"
                  class="login-button"
                  name="로그인"
                  type="submit"
                ></BasicFilled>
              </div>
              <div style="flex-shrink: 0; width: 100px; height: 100px; position: relative;"></div>
            </div>
            <div class="img-box">
              <img src="logo/login_f.png" alt="login-img">

            </div>
            <!-- <PlaceholderImage
              class="placeholder"
              src="logo/login_f.png"
            ></PlaceholderImage> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</form>
