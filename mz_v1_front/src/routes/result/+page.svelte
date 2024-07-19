<script>
  import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
  import RequestFilled from "../../components/button/request_filled.svelte";
  import PlaceholderImage from "./PlaceholderImage.svelte";
  import Header from "../../components/header/header_login.svelte";
  import StarRating from "../../components/rating/StarRating.svelte";
  import SaveImage from "../../components/button/result_save.svelte";
  import Survey from "../../components/survey/survey.svelte";
  
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  const serverIP = import.meta.env.VITE_SERVER_IP;

  let className = "";
  export { className as class };
  export let style;
  let gt_stretch_path_m = "http://223.130.133.236:9000/voice2face-public/site/result/tae_24fps_square.mp4"; 
  let gt_stretch_path_w = "http://223.130.133.236:9000/voice2face-public/site/result/hj_24fps_square.mp4"; 
  let results = [];
  let id;
  let latest_id;
  let gender;
  let token = null;
  
  onMount(async () => {
    try{
      token = sessionStorage.getItem('auth_token'); 
      gender = sessionStorage.getItem('gender');
      id = sessionStorage.getItem('id');
      latest_id = sessionStorage.getItem('latest_id');

    }
    catch(error){
      alert(`세션이 만료되었습니다.\n다시 로그인 해주세요.`);
      goto('/');
    }
    const response = await fetch(`${serverIP}/api/v1/mz-request/${id}/mz-result/${latest_id}`, {
      method: 'GET',
      headers: {
        'Token': token,
      },
    });

    if (response.ok) {
      const data = await response.json();
      results = data.mz_result; 
    } else if(response.status === 400) {
      alert("데이터베이스 에러");
    } else if (response.status === 401) {
      // Handle unauthorized
    } else {
      console.error('데이터를 가져오는 데 실패했습니다.');
      alert("요청 중 에러가 발생했습니다.")
    }
  });

  async function handleSubmit(event) {
    event.preventDefault();
  }
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
    top: 120px;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 50px;
    padding: 0px 0px 100px 0px;
    position: relative;
    width:1200px;
    margin-bottom: 60px;
  }

  .logo {
    flex-shrink: 0;
    width: 150px;
    position: relative;
    object-fit: cover;
  }

  .section {
    display: flex;
    flex-direction: row;
    gap: 82px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 1103px;
    position: relative;
  }

  .section2 {
    display: flex;
    flex-direction: row;
    gap: 82px;
    justify-content: center;
    flex-shrink: 0;
    width: 1103px;
    position: relative;
  }
  
  .column {
    display: flex;
    flex-direction: column;
    gap: 13px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
    width: 450px;
  }

  .audio-box {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
    width: 100%;
  }

  .text-box {
    left: 60px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: left;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
    width: 450px;
  }

  .text {
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 48px;
    line-height: 40px;
    font-weight: 800;
    position: relative;
  }

  .subtext {
    left: 15px;
    color: #000000;
    text-align: left;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 28px;
    line-height: 50px;
    font-weight: 600;
    position: relative;
  }

  .title-box {
    margin-top: 70px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  
  .title {
    color: #000000;
    text-align: center;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 46px;
    line-height: 40px;
    font-weight: 700;
    position: relative;
    width: 294px;
    height: 40px;
  }
  .subtitle {
    color: #8c8686;
    text-align: center;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 20px);
    line-height: var(--body-large-line-height, 32px);
    font-weight: var(--body-large-font-weight, 400);
    position: relative;
    width: 294px;
  }

  .image-frame {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    width: 340px;
    height: 340px;
    overflow: hidden;
    border-radius: 5%;
  }
  .video-frame {
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    width: 340px;
    height: 340px;
    overflow: hidden;
    border-radius: 5%;
  }

  .rating-save {
    display: flex;
    flex-direction: row;
    gap: 11px;
    align-items: flex-end;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .service-title {
    color: #000000;
    text-align: center;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 52px;
    line-height: 76px;
    font-weight: 700;
    position: relative;
  }
  .service-description {
    color: #8c8686;
    text-align: center;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 20px);
    line-height: var(--body-large-line-height, 32px);
    font-weight: var(--body-large-font-weight, 400);
    position: relative;
  }
  .videos {
    display: flex;
    flex-direction: row;
    gap: 77px;
    align-items: flex-end;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }
  .video-container {
    flex-shrink: 0;
    width: 393px;
    height: 498px;
    position: relative;
  }
  .video-title {
    color: #000000;
    text-align: center;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 46px;
    line-height: 40px;
    font-weight: 700;
    position: relative;
    width: 294px;
    height: 40px;
  }
  .video-subtitle {
    color: #8c8686;
    text-align: center;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 20px);
    line-height: var(--body-large-line-height, 32px);
    font-weight: var(--body-large-font-weight, 400);
    position: relative;
    width: 294px;
  }

  .action-box {
    margin-top: 30px;
    display: flex;
    flex-direction: row;
    gap: 48px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    width: 100%;
  }

  .survey-title {
    color: #000000;
    text-align: center;
    font-family: 'DmSans-Bold', sans-serif;
    font-size: 52px;
    line-height: 76px;
    font-weight: 700;
    position: relative;
    width: 742px;
    height: 65px;
  }
  .survey-description {
    text-align: center;
    font-size: 20pt;
  }
  .survey-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 100%;
  }

  @media (max-width: 420px) {
    .frame { 
      align-items: center;
      background-color: #fff;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      position: relative;
      width: 100%;
    }

    .main-container {
      top: 120px;
      width: 100%;
      padding: 0px 16px 60px 16px;
      align-items: center; 
      display: flex; 
      flex-direction: column; 
      margin-bottom: 30px;
    }

    .logo {
      width: 150px;
    }
    .section {
      flex-direction: column;
      width: 100%;
      gap: 20px;
    }

    .section2 {
      flex-direction: column;
      width: 100%;
      gap: 40px;
    }
    
    .column {
      width: 100%;
    }

    .text-box {
      width: 100%;
      left: 0;
      bottom: 30px;
    }

    .text {
      font-size: 32px;
      line-height: 36px;
      width: 100%;
      text-align: center;
    }

    .subtext {
      font-size: 24px;
      line-height: 36px;
      width: 100%;
      text-align: center;
    }

    .image-frame, .video-frame {
      width: 100%;
      height: auto;
    }
    .title-box {
      margin-top: 70px;
      gap: 16px;
    }
    .title {
      font-size: 30px;
      line-height: 36px;
      width: 100%;
      text-align: center;
    }
    .subtitle {
      font-size: 18px;
      width: 100%;
    }
    .service-title {
      font-size: 32px;
      line-height: 36px;
      width: 100%;
      font-weight: 800;
      text-align: center;
    }

    .service-description {
      font-size: 18px;
    }
    .action-box {
      flex-direction: column;
      gap: 20px;
    }
    .survey-title {
      font-size: 36px;
      width: 100%;
    }
    .survey-description {
      font-size: 16pt;
    }
  }
</style>

<div class="frame">
  <div class="main-container">
    <Header />
    <img class="logo" src="/logo/logo.png" alt="logo" />

      <div class="section">
        <div class="column">
        <div class="text-box">
            <div class="text">
              내 목소리 새로운 얼굴,
            </div>
            <div class="subtext">
              ddd@gmail.com 님의 요청으로<br>
              20 세 여성으로<br>
              얼굴을 생성했어요.
            </div>
            <div class="audio-box">
              <audio controls>
                <source src="path_to_audio_file" type="audio/mpeg">
                Your browser does not support the audio element.
              </audio>
            </div>
          </div>
        </div>

        <div class="column">
            <div class="image-frame">
              <PlaceholderImage targetPath={results.condition_image_url}></PlaceholderImage>
            </div>
          <div class="rating-save">
            <StarRating ABtype="condition" result_id={id} latest_id={latest_id} />
            <SaveImage targetImage={results.condition_image_url} />
          </div>
        </div>
      </div>

      <div class="title-box">
        <div class="service-title">
          Service In Video
        </div>
        <div class="service-description">
          생성된 이미지를 영상에 입힐 수 있습니다. <br>
          꾹 눌러서 저장하고 공유해 보세요!
        </div>
      </div>

      <div class="section2">
        <div class="column">
          <div class="title">Original</div>
          <div class="subtitle">원본 영상</div>
            <div class="image-frame">
              <PlaceholderImage targetPath={results.voice_image_url}></PlaceholderImage>
            </div>
        </div>

        <div class="column">
          <div class="title">Voice</div>
          <div class="subtitle">생성된 얼굴로 합성된 영상</div>
            <div class="image-frame">
              <PlaceholderImage targetPath={results.condition_image_url}></PlaceholderImage>
            </div>
          <div class="rating-save">
            <StarRating ABtype="condition" result_id={id} latest_id={latest_id} />
            <SaveImage targetImage={results.condition_image_url} />
          </div>
        </div>
      </div>

        <div class="action-box">
          <RequestFilled styleVariant="filled" style="background: var(--7b95b7, #6b6b6b); width: 190px;" name="다시 생성하기"></RequestFilled>
          <RequestFilled styleVariant="filled" style="background: var(--7b95b7, #6b6b6b); width: 190px;" name="설문조사"></RequestFilled>
          <ButtonStyleFilled styleVariant="filled" style="background: var(--7b95b7, #6b6b6b); width: 190px;" targetPath="/resultlist" name="결과 목록 보기"></ButtonStyleFilled>
        </div>

    </div>
    {#if results.survey == 0}
      <div class="survey-title">설문조사</div>
      <div class="survey-description">
        안녕하세요! 사용자의 목소리를 기반으로 가상의 얼굴을 생성하는 서비스, <br>
        <span><strong>Voice2Face</strong></span>를 개발 중인 <span><strong>Make Zenerator</strong></span>팀입니다.
        <br><br>
        저희는 온라인 상에서 얼굴을 드러내고 싶지 않은 사람들에게 목소리를 기반으로 생성한 얼굴을 제공하여, 
        <br />
        목소리와 이미지 간의 이질감을 없애고 사생활을 보장받으며 온라인 상에서 활동할 수 있도록 하는 서비스를 제공하고자 합니다.
        <br>
        <br />
        서비스 품질 향상을 위해 지금까지의 서비스 이용 경험을 바탕으로 아래의 설문 조사에 참여해주시면 감사드리겠습니다.
        <br />
        설문 예상 소요 시간은 <span><strong>약 5분 내외</strong></span>이며  
        <br /> 
        참여하신 분들 중 추첨을 통해 5분께 <span><strong>스타벅스 카페 아메리카노</strong></span> 기프티콘을 드릴 예정입니다.
        <br />
        (설문은 생성된 이미지 결과별로 제출할 수 있습니다.)
      </div>
      <div class="survey-container">
        <Survey survey_id={id} survey_latest_id={latest_id} star_rating={star_rating} />
      </div>
    {/if}
  </div>
