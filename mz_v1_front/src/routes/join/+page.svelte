<script>
  import BasicFilled from "../../components/button/basic_filled.svelte";
  import PlaceholderImage from "./PlaceholderImage.svelte";
  import Header from "../../components/header/header_login.svelte";
  import HeaderNon from "../../components/header/header_non.svelte";
  import Radio from "./radio.svelte"
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  export let targetPath = "/";
  let className = "";
  export { className as class };
  export let style;
  let join_email;
  let join_pswd;
  let join_check;
  let join_gender;
  let join_age;
  let join_agree = false;
  let passwordMismatch = false;

  let token = null;
  let isLoggedIn = false;
  let sessionChecked = false;

  function checkSession() {
    console.log('세션 토큰 확인 중...');
    token = sessionStorage.getItem('auth_token');
    console.log('토큰:', token);
    if (token) {
      isLoggedIn = true;
      goto('/home')
      ;
    }
    sessionChecked = true
  }

  onMount(() => {
    checkSession();
  });

  const serverIP = import.meta.env.VITE_SERVER_IP;

  const options = [{
    value: 'man',
    label: '남',
  }, {
    value: 'woman',
    label: '여',
  }]

  $: {
    if (join_pswd !== join_check && join_check) {
      passwordMismatch = true;
    } else {
      passwordMismatch = false;
    }
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (!join_agree) {
      alert("개인정보 수집 이용에 동의를 체크해주셔야 서비스를 이용하실 수 있습니다.");
      return;
    }

    if (join_pswd !== join_check) {
      alert("비밀번호가 일치하지 않습니다.");
      return;
    }

    const formData = new FormData();
    formData.append('email', join_email);
    formData.append('password', join_pswd);
    formData.append('age', join_age);
    formData.append('gender', join_gender);

    try {
      const response = await fetch(`${serverIP}/api/v1/users`, {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const result = await response.json();
        console.log('회원가입 성공:', result);
        alert("회원가입 완료했습니다!!");
        goto(targetPath); // 성공 시 리디렉션

      } else if (response.status === 409) {
        alert(`이메일이 중복되었습니다. 다른 이메일을 입력해주세요.`);
      }
      else {
        const error = await response.json();
        alert(`회원가입 실패: ${error.message}`);
      }
    } catch (error) {
      console.error('회원가입 중 에러 발생:', error);
      alert('회원가입 중 에러가 발생했습니다.');
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
    top: 160px;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 99px;
    padding: 0px 0px 120px 0px;
    position: relative;
    width:1200px;
  }

  .inner-content {
    display: flex;
    flex-direction: row;
    gap: 41px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .inner-content-center {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 46px;
  }

  .signup-box {
    background: #ffffff;
    border-radius: 10px;
    border-style: solid;
    border-color: #878787;
    border-width: 0.5px;
    padding: 47px 0px 80px 0px;
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: center;
    flex-shrink: 0;
    width: 451px;
    position: relative;
    box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
    overflow: hidden;
  }

  .img-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .signup-content {
    display: flex;
    flex-direction: column;
    gap: 43px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    height: 822px;
    position: relative;
  }

  .signup-header {
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
    gap: 22px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .input-field-group {
    display: flex;
    flex-direction: column;
    gap: 13px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .input-field {
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
    font-size: 14px;
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

  .radio-group {
    display: flex;
    flex-direction: row;
    gap: 18px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 337px;
    position: relative;
  }

  .textarea {
    overflow-y: auto;
    background: #ffffff;
    border-radius: 10px;
    border: 1px solid #000000;
    padding: 10px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    justify-content: flex-start;
    width: 337px;
    height: 158px;
    max-height: 200px;
    color: rgba(0, 0, 0, 0.87);
    text-align: left;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 12px;
    line-height: 15px;
    font-weight: 500;
    margin: 0px;
  }

  .checkbox-label {
    display: flex;
    align-items: center;
    cursor: pointer;
  }

  .checkbox-container {
    display: flex;
    justify-content: flex-end;
    width: 100%;
  }

  .signup-button {
    background: var(--7b95b7, #6b6b6b);
    flex-shrink: 0;
  }

  .placeholder-image {
    flex-shrink: 0;
    width: 600px;
  }

  @media(max-width: 1120px) {
  .main-container {
    padding-bottom: 80px;
  }

  .inner-content-center{
    flex-direction: column;
  }
}

  @media(max-width: 420px) {
  form {
    gap: 60px;
  }

  .frame {
    width: 100%;
    padding: 0 16px;
  }

  .main-container {
    top: 120px;
    width: 100%;
    padding: 0;
    gap: 80px;
    align-items: center;
  }

  /* form {
    padding: 0px 16px 80px 16px;
    gap: 60px;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center; 
  }

  .frame {
    padding: 0 16px;
  }

  .main-container {
    top: 120px;
    width: 100%;
    padding: 0;
    gap: 60px;
    align-items: center;
    margin-bottom: 60px;
  } */

  .inner-content {
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
  }

  .inner-content-center {
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
  }

  .signup-box {
    width: 100%;
    padding: 45px 20px 90px 20px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .signup-content {
    width: 100%;
    gap: 28px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .signup-header {
    font-size: 32px;
    line-height: 36px;
    width: 100%;
    text-align: center;
  }

  .input-group {
    width: 100%;
    gap: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-field-group {
    width: 100%;
    gap: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-field {
    width: 100%;
    gap: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .input-label {
    font-size: 16px;
    line-height: 20px;
    width: 100%;
    text-align: center;
  }

  .input-box {
    width: 100%;
    padding: 1px 20px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .input {
    font-size: 16px;
    line-height: 24px;
    text-align: center;
  }

  .radio-group {
    width: 100%;
    justify-content: center;
    left: 42px;
  }

  .textarea {
    width: 100%;
    height: auto;
    max-height: 200px;
    padding: 10px;
    box-sizing: border-box;
  }

  .checkbox-container {
    width: 100%;
    justify-content: center;
  }

  .signup-button {
    width: 100%;
    margin-bottom: 20px;
  }

  .img-box {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .placeholder-image {
    width: 100%;
    max-width: 300px;
    height: auto;
  }
}


</style>

{#if sessionChecked}
<form on:submit|preventDefault={handleSubmit} class="form-container" style={style}>
  <div class="frame">
    <div class="main-container">
      {#if isLoggedIn}
        <Header />
      {:else}
        <HeaderNon />
      {/if} 
      <div class="inner-content">
        <div class="inner-content-center">
          <div class="signup-box">
            <div class="signup-content">
              <div class="signup-header">회원가입</div>
              <div class="input-group">
                <div class="input-field-group">
                  <div class="input-field">
                    <div class="input-label">이메일 주소</div>
                    <div class="input-box">
                      <input type='email' bind:value={join_email} placeholder="이메일 입력" class="input" />
                    </div>
                  </div>
                  <div class="input-field">
                    <div class="input-label">비밀번호</div>
                    <div class="input-box">
                      <input type='password' bind:value={join_pswd} placeholder="비밀번호 입력" class="input" />
                    </div>
                  </div>
                  <div class="input-field">
                    <div class="input-label">비밀번호 확인</div>
                    <div class="input-box">
                      <input type='password' bind:value={join_check} placeholder="비밀번호 입력" class="input" />
                    </div>
                  </div>
                  <div class="input-field">
                    <div class="input-label">성별</div>
                    <div class="radio-group">
                      <Radio {options} fontSize={20} legend='' bind:userSelected={join_gender} />
                    </div>
                  </div>
                  <div class="input-field">
                    <div class="input-label">나이</div>
                    <div class="input-box">
                      <input type="number" bind:value={join_age} min=0 max=120 class="input" placeholder="나이 입력" />
                    </div>
                  </div>
                </div>
                <div class="input-field-group">
                  <div class="input-field">
                    <div class="input-label" style="width: 339px;">개인정보 수집 이용 동의서</div>
                    <div class="textarea">
                      <p><strong>본인은 아래와 같이 개인정보의 수집 및 이용에 동의합니다.</strong></p>

                      <p><strong>1. 수집하는 개인정보의 항목:</strong></p>
                      <ul>
                        <li>이메일 (Email)</li>
                        <li>성별 (Gender)</li>
                        <li>나이 (Age)</li>
                        <li>목소리 (Voice)</li>
                      </ul>

                      <p><strong>2. 개인정보의 수집 및 이용 목적:</strong></p>
                      <ul>
                        <li>회원 서비스 제공을 위한 이메일 통보 및 연락</li>
                        <li>회원의 특성에 따른 맞춤형 서비스 제공</li>
                        <li>목소리 데이터를 활용한 얼굴 생성 기술 개발 및 서비스 향상</li>
                        <li>수집된 데이터를 기반으로 한 모델 학습을 통한 개선된 서비스 제공</li>
                      </ul>

                      <p><strong>3. 개인정보의 보유 및 이용 기간:</strong></p>
                      <p>개인정보 수집 및 이용 목적 달성 후 즉시 파기합니다. 단, 관련 법령에 따라 보존할 필요가 있는 경우에는 해당 법령의 규정에 따라 보존합니다.</p>

                      <p><strong>4. 동의 거부 권리:</strong></p>
                      <p>본인은 개인정보 제공에 대한 동의를 거부할 권리가 있습니다. 단, 필수 항목에 대한 동의를 거부할 경우 회원 가입이 제한될 수 있습니다.</p>

                      <p><strong>본인은 위와 같이 개인정보 수집 및 이용에 동의합니다.</strong></p>
                    </div>
                    <div class="checkbox-container">
                      <label class="checkbox-label">
                        <input type="checkbox" bind:checked={join_agree}>
                        <span style="margin-left: 8px; margin-right: 8px;">동의함</span>
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <BasicFilled
                styleVariant="filled"
                style="background: var(--7b95b7, #6b6b6b); flex-shrink: 0"
                class="signup-button"
                name="회원가입"
                type="submit"
              ></BasicFilled>
            </div>
          </div>
          <div class="img-box">
            <PlaceholderImage
              style="width: 420px;"
              class="placeholder-image"
              targetPath="logo/join.png"
            ></PlaceholderImage>
          </div>
        </div>
      </div>
    </div>
  </div>
</form>
{:else}
<div></div>
{/if}