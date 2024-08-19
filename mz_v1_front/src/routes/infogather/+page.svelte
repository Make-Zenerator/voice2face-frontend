<script>
  import BasicButton from "../../components/button/basic_filled.svelte";
  import VoiceButtonDefaultVariant3 from "./VoiceButtonDefaultVariant3.svelte";
  import { Progressbar } from 'flowbite-svelte';
  import { sineOut } from 'svelte/easing';
  import Radio from "../join/radio.svelte";
  import Header from "../../components/header/header_login.svelte";
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';

  export { className as class };
  export let style;
  export let targetPath = "/loading";

  let className = "";
  let info_gender;
  let info_age;
  let info_video;
  
  let progress = 0;
  let audioUrl = '';
  let audioBlob = null;
  let token; 

  const genderOptions = [{
    value: 'man',
    label: '남',
  }, {
    value: 'woman',
    label: '여',
  }];

  const videoOptions = [{
    value: 'video1',
    label: '킹스맨',
    image: '/_src_temp/video1.png' // 이미지 경로를 수정
  }, {
    value: 'video2',
    label: '예나',
    image: '/_src_temp/video2.png' // 이미지 경로를 수정
  }, {
    value: 'video3',
    label: '사딸라',
    image: '/_src_temp/video3.png' // 이미지 경로를 수정
  }, {
    value: 'video4',
    label: '연진아',
    image: '/_src_temp/video4.png' // 이미지 경로를 수정
  }];

  onMount(() => {
    try {
      token = sessionStorage.getItem('auth_token');
    } catch (error) {
      alert(`세션이 만료되었습니다.\n다시 로그인 해주세요.`);
      goto('/');
    }
  });

  async function requestImage() {
    const formData = new FormData();
    formData.append('age', info_age);
    formData.append('gender', info_gender);
    formData.append('video', info_video);
    if (audioBlob) {
      formData.append('file', audioBlob, 'svelte_audio.wav');
    }

    try {
      const serverIP = import.meta.env.VITE_SERVER_IP;
      console.log(serverIP)
      const response = await fetch(`${serverIP}/api/v1/mz-request`, {
        method: 'POST',
        headers: {
          'Token': token,
        },
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        alert(`성공적으로 요청했습니다.`);
        goto(targetPath); 
      } else if (response.status === 401) {
        alert(`세션이 만료되었습니다.\n다시 로그인 해주세요.`);
        goto('/');
      } else if (response.status === 400) {
        alert("데이터베이스 에러");
      } else if (response.status === 405){
          alert("생성횟수가 10회를 초과하여 요청실패 되었습니다.")
      } else if (response.status === 404){
        alert("나이, 성별, 비디오, 음성 파일 중 누락된 것이 있습니다.")
      }else {
        const errorResponse = await response.json(); 
        alert(`요청 실패: ${errorResponse.message}`);
        console.log(response);
      }
    } catch (error) {
      console.error('생성 요청 중 에러 발생:', error);
      alert('요청 중 에러가 발생했습니다.');
    }
  }

  let showExample = false; 

  function toggleExample() {
    showExample = !showExample; 
  }
</script>

<style>
  form {
    background: var(--neutral-0, #ffffff);
    padding: 0px 0px 120px 0px;
    display: flex;
    flex-direction: column;
    gap: 120px;
    align-items: center;
    justify-content: flex-start;
    position: relative;
  }

  .frame {
    align-items: center;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    position: relative;
  }

  .main-container {
    top: 220px;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 99px;
    padding: 0px 0px 120px 0px;
    position: relative;
    width: 1200px;
  }

  .inner-content {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .left-panel {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    height: 800px;
    position: relative;
  }
  .form-box {
    background: #ffffff;
    border-radius: 10px;
    border-style: solid;
    border-color: #878787;
    border-width: 0.5px;
    padding: 20px 0px 60px 0px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 451px;
    position: relative;
    box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
    overflow: hidden;
  }
  .title-container {
    display: flex;
    flex-direction: column;
    gap: 4px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    height: 83px;
    position: relative;
    margin-top: 10px;
  }
  .title {
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

  .title-description {
    display: none;
    font-size: 16px;
    line-height: 24px;
    text-align: center;
    color: #6b6b6b;
  }

  .input-container {
    display: flex;
    flex-direction: column;
    gap: 14px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  .input-box {
    display: flex;
    flex-direction: column;
    gap: 15px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 331px;
    position: relative;
  }
  .label {
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 19px;
    line-height: 40px;
    font-weight: 500;
    position: relative;
    width: 331px;
    height: 25px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-top: 10px;
  }
  .radio-container {
    display: flex;
    flex-direction: row;
    gap: 18px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 337px;
    height: 18px;
    position: relative;
  }
  .age-label {
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 19px;
    line-height: 40px;
    font-weight: 500;
    position: relative;
    width: 337px;
    height: 26px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
  }
  .age-input-container {
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
    justify-content: center;
    flex-shrink: 0;
    width: 337px;
    height: 46px;
    position: relative;
    overflow: hidden;
  }
  .age-input {
    color: rgba(0, 0, 0, 0.87);
    text-align: center;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 14px;
    line-height: 40px;
    font-weight: 500;
    border: none;
    width: 100%;
    height: 40px;
    background: transparent;
    -webkit-appearance: none;
    margin: 0;
  }
  .voice-label {
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 19px;
    line-height: 40px;
    font-weight: 500;
    position: relative;
    width: 337px;
    height: 21px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-top: 30px;
  }

  .voice-container {
    display: flex;
    flex-direction: row;
    gap: 40px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 337px;
    position: relative;
    padding-right: 20px;
  }

  .video-label {
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Medium', sans-serif;
    font-size: 19px;
    line-height: 40px;
    font-weight: 500;
    position: relative;
    width: 337px;
    height: 21px;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-top: 50px;
  }

  .video-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 337px;
    position: relative;
  }
  .video-option {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 100%;
  }
  .video-option img {
    width: 150px;
    height: 100px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 10px;
  }
  .video-option input[type="radio"] {
    position: absolute;
    opacity: 0;
  }
  .video-option label {
    display: flex;
    flex-direction: column;
    align-items: center;
    cursor: pointer;
  }

.video-option input[type="radio"] + label {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  position: relative;
}
.video-option input[type="radio"] + label::before {
  content: "";
  position: relative;
  display: inline-block;
  width: 1em;
  height: 1em;
  background: transparent;
  border: 1px solid var(--gray, #ccc);
  border-radius: 50%;
  top: 0.2em;
  margin-bottom: 0.5em;
}
.video-option input[type="radio"]:checked + label::before {
  border: 1px solid var(--gray, #ccc);
  border-radius: 50%;
}
.video-option input[type="radio"] + label::after {
  content: "";
  position: absolute;
  display: inline-block;
  width: 0.5em;
  height: 0.5em;
  top: 0.45em;
  left:4.42em;
  background: var(--accent-color, #282828);
  border: 1px solid var(--accent-color, #282828);
  border-radius: 50%;
  transform: scale(0);
  transition: transform 0.2s ease-in-out;
}
.video-option input[type="radio"]:checked + label::after {
  transform: scale(1);
}
.video-option input[type="radio"]:focus + label::before {
  box-shadow: 0 0 0 1px var(--accent-color, #282828);
  border-radius: 50%;
}
  .video-option input[type="radio"]:disabled + label {
    color: darken(var(--gray, #ccc), 10);
  }
  .video-option input[type="radio"]:disabled + label::before {
    background: var(--gray, #ccc);
  } 
  .video-option input[type="radio"] + label::before {
    transition: background 0.3s ease-out;
  }
  .video-option input[type="radio"]:checked + label::before {
    transition: background 0.3s ease-in;
  }
  .video-option input[type="radio"] + label::after {
    transition: transform 0.2s ease-out;
  }
  .video-option input[type="radio"]:checked + label::after {
    transition: transform 0.2s ease-in;
  }
  .video-option input[type="radio"]:focus + label::before {
    box-shadow: 0 0px 8px var(--accent-color, #282828);
    border-radius: 50%;
  }





  .note-container {
    width: 302px;
    margin-top: 20px;
  }
  .example-container {
    width: 302px;
    margin-top: 20px;
  }
  .right-panel {
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  .right-panel-inner {
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  .right-panel-title-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  .right-panel-title {
    color: var(--6b6b6b, #000000);
    text-align: center;
    font-family: var(--title-large-font-family, 'DmSans-Bold', sans-serif);
    font-size: var(--title-large-font-size, 60px);
    line-height: var(--title-large-line-height, 76px);
    font-weight: var(--title-large-font-weight, 700);
    position: relative;
  }
  .right-panel-description {
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 20px);
    line-height: var(--body-large-line-height, 32px);
    font-weight: var(--body-large-font-weight, 400);
    position: relative;
    align-self: stretch;
  }
  .button-container {
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  .submit-button {
    background: var(--6b6b6b, #000000);
    border-color: var(--6b6b6b, #000000);
    flex-shrink: 0;
    width: 143px;
  }


  @media (max-width: 1120px) {

    .inner-content {
      flex-direction: column;
      /* gap: 20px;
      align-items: center;
      width: 100%; */
    }

    /* .left-panel, .right-panel {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }

    .right-panel {
      top: 150px;
      padding-bottom: 60px;
    }

    .form-box {
      width: 100%;
      padding: 20px 20px 50px 20px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .title-container {
      top: 5px;
    }

    .title-container, .right-panel-title-container {
      width: 100%;
      text-align: center;
    }

    .title, .right-panel-title {
      font-size: 32px;
      line-height: 36px;
      width: 100%;
      text-align: center;
    }

    .title-description {
      display: flex;
    }

    .input-container, .input-box, .right-panel-inner, .button-container {
      width: 100%;
      align-items: center;
      gap: 20px;
    }

    .label, .age-label, .voice-label , .video-label{
      font-size: 16px;
      line-height: 20px;
      width: 100%;
      text-align: center;
    }

    .voice-container {
      gap: 30px;
      padding-right: 20px;
    }

    .radio-container, .age-input-container, .voice-container {
      width: 100%;
      justify-content: center;
    }

    .radio-container {
      left: 42px;
    }

    .age-input {
      font-size: 16px;
      line-height: 24px;
      text-align: center;
    } */

    /* .note-container, .example-container {
      width: 100%;
      padding-left: 10px;
    }

    .submit-button {
      width: 100%;
    } */

    .right-panel-title-container {
      display: none;
    }
    .right-panel-description {
      display: none;
    }

    .button-container {
      margin-top: 10px;
      margin-bottom: 30px;
    }


    /* .video-option input[type="radio"] + label::after {
      content: "";
      position: absolute;
      display: inline-block;
      width: 0.5em;
      height: 0.5em;
      top: 0.45em;
      left:4.44em;
      background: var(--accent-color, #282828);
      border: 1px solid var(--accent-color, #282828);
      border-radius: 50%;
      transform: scale(0);
      transition: transform 0.2s ease-in-out;
    } */
  }

  @media (max-width: 420px) {
    form {
      padding: 0px 16px 40px 16px;
      gap: 40px;
      height: auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
    }

    .frame {
      width: 100%;
    }

    .main-container {
      top: 120px;
      width: 100%;
      padding: 0;
      gap: 60px;
      align-items: center;
      margin-bottom: 60px;
    }

    .inner-content {
      flex-direction: column;
      gap: 20px;
      align-items: center;
      width: 100%;
    }

    .left-panel, .right-panel {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
    }

    .right-panel {
      top: 150px;
      padding-bottom: 60px;
    }

    .form-box {
      width: 100%;
      padding: 20px 20px 50px 20px;
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .title-container {
      top: 5px;
    }

    .title-container, .right-panel-title-container {
      width: 100%;
      text-align: center;
    }

    .title, .right-panel-title {
      font-size: 32px;
      line-height: 36px;
      width: 100%;
      text-align: center;
    }

    .title-description {
      display: flex;
    }

    .input-container, .input-box, .right-panel-inner, .button-container {
      width: 100%;
      align-items: center;
      gap: 20px;
    }

    .label, .age-label, .voice-label , .video-label{
      font-size: 16px;
      line-height: 20px;
      width: 100%;
      text-align: center;
    }

    .voice-container {
      gap: 30px;
      padding-right: 20px;
    }

    .radio-container, .age-input-container, .voice-container {
      width: 100%;
      justify-content: center;
    }

    .radio-container {
      left: 42px;
    }

    .age-input {
      font-size: 16px;
      line-height: 24px;
      text-align: center;
    }

    .note-container, .example-container {
      width: 100%;
      padding-left: 10px;
    }

    .submit-button {
      width: 100%;
    }

    .right-panel-title-container {
      display: none;
    }
    .right-panel-description {
      display: none;
    }

    .button-container {
      margin-top: 10px;
      margin-bottom: 30px;
    }


    .video-option input[type="radio"] + label::after {
      content: "";
      position: absolute;
      display: inline-block;
      width: 0.5em;
      height: 0.5em;
      top: 0.45em;
      left:4.44em;
      background: var(--accent-color, #282828);
      border: 1px solid var(--accent-color, #282828);
      border-radius: 50%;
      transform: scale(0);
      transition: transform 0.2s ease-in-out;
    }
  }
</style>

<form on:submit|preventDefault={requestImage} class="form-container" style={style}>
  <div class="frame">
    <div class="main-container">
      <Header />
      <div class="inner-content">
        <div class="left-panel">
          <div class="form-box">
            <div class="title-container">
              <div class="title">생성하기</div>
              <div class="title-description">나의 성별, 나이, 목소리를 입력해주세요</div>
            </div>
            <div class="input-container">
              <div class="input-box">
                <div class="label">성별</div>
                <div class="radio-container">
                  <Radio options={genderOptions} fontSize={20} legend='' bind:userSelected={info_gender} />
                </div>
              </div>
              <div class="age-label">나이</div>
              <div class="age-input-container">
                <input
                  type="number"
                  bind:value="{info_age}"
                  min="20"
                  max="50"
                  class="age-input"
                  placeholder="나이 입력"
                />
              </div>
              <div class="voice-label">목소리</div>
              <div class="voice-container">
                <VoiceButtonDefaultVariant3 
                  on:audioRecorded={(event) => { audioUrl = event.detail; }} 
                  on:progressUpdated={(event) => { progress = event.detail; }}
                  on:blobUpdated={(event) => { audioBlob = event.detail; }}
                />
                {#if audioUrl == ''}
                  <Progressbar {progress} animate precision={2} tweenDuration={15100} easing={sineOut} size="h-6" />
                {:else}
                  <audio controls src={audioUrl}></audio>
                {/if}
              </div>
              <div class="video-label">합성 영상 선택</div>
              <div class="video-options">
                {#each videoOptions as option}
                <div class="video-option">
                  <input type="radio" id={option.value} name="video" value={option.value} bind:group={info_video} />
                  <label for={option.value}>
                    <img src={option.image} alt={option.label} />
                    <div>{option.label}</div>
                  </label>
                </div>
                {/each}
              </div>
            </div>
          </div>
        </div>
        <div class="right-panel">
          <div class="right-panel-inner">
            <div class="right-panel-title-container">
              <div class="right-panel-title">얼굴 생성하기</div>
            </div>
            <div class="right-panel-description">나의 성별, 나이, 목소리를 입력해주세요</div>
          </div>
          <div class="button-container">
            <BasicButton
              styleVariant="filled"
              style="
              background: var(--6b6b6b, #000000);
              border-color: var(--6b6b6b, #000000);
              flex-shrink: 0;
              width: 143px;
            "
              class="submit-button"
              name="생성하기"
              type="submit"
            ></BasicButton>
          </div>
          <div class="note-container">
            <strong>주의사항</strong><br/>
            1. 마이크가 제대로 작동하는지 확인해주세요. <br/>
            2. 조용한 장소에서 녹음해주세요. <br/>
            3. 마이크를 누르면 <strong>1초 뒤</strong> 녹음을 시작합니다.<br/>
            4. 10초 동안 아무 말이나 해주세요. <br />
            5. <strong>목소리 주인공</strong>의 성별과 나이를 입력해주세요.<br />
            6. 생성 횟수는 <strong>10회</strong>로 제한합니다.
          </div>
          <div class="example-container">
            <strong>예시문장</strong><br/>
            안녕하세요, 저희는 엠지 팀입니다. <br/>
            현재 목소리를 통해 얼굴을 만들어주는 <br/>
            프로젝트를 진행하고 있습니다. <br/>
            내 목소리의 또 다른 나를 만들어보세요!
          </div>
        </div>
      </div>
    </div>
  </div>
</form>
