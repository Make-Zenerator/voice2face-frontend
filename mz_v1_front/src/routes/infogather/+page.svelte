<script>
  import BasicButton from "../../components/button/basic_filled.svelte";
  import VoiceButtonDefaultVariant3 from "./VoiceButtonDefaultVariant3.svelte";
  import { Progressbar, Button } from 'flowbite-svelte';
  import { sineOut } from 'svelte/easing';
  import Radio from "../join/radio.svelte";
  import Header from "../../components/header/header_login.svelte"
  export { className as class };
  export let style;
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';

  export let targetPath = "/loading";

  let className = "";
  let info_gender;

  let info_age;
  let progress = 0;

  let audioUrl = '';
  let audioBlob= null;
  let token; 
  const options = [{
		value: 'man',
		label: '남',
	},  {
		value: 'woman',
		label: '여',
	}]

  onMount(() => {
    try{token = sessionStorage.getItem('auth_token');}
    catch(error){
      alert(`세션이 만료되었습니다.\n다시 로그인 해주세요.`);
      goto('/');
    }
    

  });


  async function requestimage(){
    const formData = new FormData();
    formData.append('age', info_age);
    formData.append('gender', info_gender);
    if (audioBlob) {
      console.log(typeof(audioBlob));
    formData.append('file', audioBlob, 'svelte_audio.wav');
  }

    try{
        const response = await fetch('http://api.makezenerator.com/api/v1/mz-request', {
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
        } else if (response.status === 401){
          alert(`세션이 만료되었습니다.\n다시 로그인 해주세요.`);
          goto('/');
        } else if (response.status === 400){
          alert("데이터베이스 에러");
        }
        else {
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

<form on:submit|preventDefault={requestimage} style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 120px; align-items: center; justify-content: flex-start; height: 900px; position: relative; ' + style}">

  <div
  style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 60px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
>

  <Header/>
  <div
    style="
      display: flex;
      flex-direction: row;
      gap: 82px;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      width: 1103px;
      height: 800px;
      position: relative;
    "
  >
    <div
      style="
        display: flex;
        flex-direction: row;
        gap: 82px;
        align-items: center;
        justify-content: flex-start;
        flex-shrink: 0;
        height: 800px;
        position: relative;
      "
    >
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 82px;
          align-items: flex-start;
          justify-content: flex-start;
          flex-shrink: 0;
          height: 675px;
          position: relative;
        "
      >
        <div
          style="
            background: #ffffff;
            border-radius: 10px;
            border-style: solid;
            border-color: #878787;
            border-width: 0.5px;
            padding: 47px 0px 47px 0px;
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
          "
        >
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 20px;
              align-items: center;
              justify-content: center;
              flex-shrink: 0;
              height: 83px;
              position: relative;
            "
          >
            <div
              style="
                display: flex;
                flex-direction: column;
                gap: 20px;
                align-items: center;
                justify-content: center;
                flex-shrink: 0;
                position: relative;
              "
            >
              <div
                style="
                  color: #000000;
                  text-align: center;
                  font-family: 'DmSans-Bold', sans-serif;
                  font-size: 46px;
                  line-height: 40px;
                  font-weight: 700;
                  position: relative;
                  width: 451px;
                  height: 40px;
                "
              >
                생성하기
              </div>
            </div>
          </div>
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 14px;
              align-items: flex-start;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          > 
            <div
              style="
                display: flex;
                flex-direction: column;
                gap: 15px;
                align-items: flex-start;
                justify-content: flex-start;
                flex-shrink: 0;
                width: 331px;
                position: relative;
              "
            >
              <div
                style="
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
                "
              >
                성별
              </div>
              <div
                style="
                  display: flex;
                  flex-direction: row;
                  gap: 18px;
                  align-items: center;
                  justify-content: center;
                  flex-shrink: 0;
                  width: 337px;
                  height: 18px;
                  position: relative;
                "
              >
              <Radio {options} fontSize={20} legend='' bind:userSelected={info_gender}/>
              </div>
            </div>
            <div
              style="
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
              "
            >
              나이
            </div>
            <div
  style="
    background: #ffffff;
    border-radius: 10px;
    border-style: solid;
    border-color: #000000;
    border-width: 1px;
    padding: 1px 43px 1px 43px;
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
  "
>
  <input
    type="number"
    bind:value="{info_age}"
    min=20
    max=50
    style="
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
    "

    placeholder="나이 입력" 
  />
</div> 

            <div
              style="
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
              "
            >
              목소리
            </div>
            <div
              style="
                display: flex;
                flex-direction: row;
                gap: 57px;
                align-items: center;
                justify-content: flex-start;
                flex-shrink: 0;
                width: 337px;
                position: relative;
              "
            >
            <VoiceButtonDefaultVariant3 
            on:audioRecorded={(event) => {
              audioUrl = event.detail;
            }} 
            on:progressUpdated={(event) => {progress = event.detail;}}
            on:blobUpdated={(event) => { audioBlob = event.detail; }}
/>
            {#if audioUrl == ''}
            <Progressbar {progress}
            animate
            precision={2}
            tweenDuration={15100}
            easing={sineOut}
            size="h-6" />
          
              {:else}
                <audio controls src = {audioUrl}></audio>
              {/if}
            </div>
            <div>
              <strong>주의사항</strong><br/>
              1. 마이크가 제대로 작동하는지 확인해주세요 <br/>
              2. 조용한 장소에서 녹음해주세요 <br/>
              <strong style="color:red">3. 마이크를 누르면 1초 뒤 녹음을 시작합니다 </strong><br/>
              4. 15초 동안 아무 말이나 해주세요 <br />
            </div>
            
              <div>
                <p><strong>예시문장</strong></p>
                <p>안녕하세요, 저희는 엠지 팀입니다.</p>
                <p>현재 목소리를 통해 얼굴을 만들어주는 </p>
                <p>프로젝트를 진행하고 있습니다.</p>
                <p>내 목소리의 또 다른 나를 만들어보세요!</p>
              </div>
          </div>
        </div>
      </div>
    </div>
    <div
      style="
        display: flex;
        flex-direction: column;
        gap: 24px;
        align-items: center;
        justify-content: flex-start;
        flex-shrink: 0;
        position: relative;
      "
    >
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 16px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 8px;
            align-items: flex-start;
            justify-content: flex-start;
            flex-shrink: 0;
            position: relative;
          "
        >
          <div
            style="
              color: var(--6b6b6b, #000000);
              text-align: center;
              font-family: var(
                --title-large-font-family,
                'DmSans-Bold',
                sans-serif
              );
              font-size: var(--title-large-font-size, 60px);
              line-height: var(--title-large-line-height, 76px);
              font-weight: var(--title-large-font-weight, 700);
              position: relative;
            "
          >
            얼굴 생성하기
          </div>
        </div>
        <div
          style="
            color: var(--7b95b7, #6b6b6b);
            text-align: center;
            font-family: var(
              --body-large-font-family,
              'DmSans-Regular',
              sans-serif
            );
            font-size: var(--body-large-font-size, 20px);
            line-height: var(--body-large-line-height, 32px);
            font-weight: var(--body-large-font-weight, 400);
            position: relative;
            align-self: stretch;
          "
        >
          나의 성별, 나이, 목소리를 입력해주세요
        </div>
      </div>
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 24px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <BasicButton
          styleVariant="filled"
          style="
            background: var(--6b6b6b, #000000);
            border-color: var(--6b6b6b, #000000);
            flex-shrink: 0;
            width: 143px;
          "
          name="생성하기"
          type="submit"
        ></BasicButton>
      </div>
    </div>
  </div>
</div>
</form>