<script>
  import ButtonStyleFilled from "./join/ButtonStyleFilled.svelte";
  import ButtonStyleOutlined from "./join/ButtonStyleOutlined.svelte";
  import Header from "../components/header/header_non.svelte";

  const introVideo = import.meta.env.VITE_INTRO_VIDEO;
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
    gap: 100px;
    padding: 0px 0px 60px 0px;
    position: relative;
    width:1200px;
    margin-bottom: 60px;
  }

  .content {
    display: flex;
    flex-direction: column;
    gap: 120px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .inner-content {
    display: flex;
    flex-direction: row;
    gap: 40px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .text-column {
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 612px;
  }

  .text-group {
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .text-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .small-title {
    color: #000000;
    text-align: left;
    font-family: var(--title-small-font-family, 'DmSans-Bold', sans-serif);
    font-size: var(--title-small-font-size, 32px);
    line-height: var(--title-small-line-height, 40px);
    font-weight: var(--title-small-font-weight, 700);
    position: relative;
    width: 612px;
  }

  .large-title {
    color: #000000;
    text-align: left;
    font-family: var(--title-large-font-family, 'DmSans-Bold', sans-serif);
    font-size: var(--title-large-font-size, 60px);
    line-height: var(--title-large-line-height, 76px);
    font-weight: var(--title-large-font-weight, 700);
    position: relative;
    width: 612px;
  }

  .description {
    color: #8c8686;
    text-align: left;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 20px);
    line-height: var(--body-large-line-height, 32px);
    font-weight: var(--body-large-font-weight, 400);
    position: relative;
    width: 612px;
  }

  .button-group {
    display: flex;
    flex-direction: row;
    gap: 24px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .video {
    width: 300px;
  }

  .image-container {
    top: 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: flex-end;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .boostcamp-logo {
    flex-shrink: 0;
    width: 300px;
    height: 100%;
    position: relative;
    overflow: visible;
  }



  @media(max-width: 1140px) {
    .main-container {
      margin-bottom: 230px;
      width: 100%;
    }

    .content {
      gap: 60px;
      width: 100%;
      align-items: center;
      display: flex;
      flex-direction: column; 
      text-align: center; 
    }

    .inner-content {
      flex-direction: column;
      align-items: center;
      width: 100%;
      text-align: center; 
    }

    .text-group{
      width: 100%;
    }

    .text-block{
      width: 100%;
    }

    .small-title{
      width: 100%;
    }

    .text-column {
      width: 100%;
      align-items: center; 
      text-align: center; 
    }

    .small-title {
      text-align: center;
    }

    .large-title {
      width: 100%;
      text-align: center;
    }

    .description {
      width: 100%;
      text-align: center; 
    }


    .video {
      width: 280px;
      margin-top: 40px;
    }

  }

  @media(max-width: 720px) {
    .large-title{
      font-size: 50px;
    }

  }



  @media(max-width: 420px) {
  .main-container {
    top: 150px;
    width: 100%;
    padding: 0px 16px 60px 16px;
    align-items: center; 
    display: flex; 
    flex-direction: column; 
    margin-bottom: 30px;
  }

  .content {
    gap: 60px;
    align-items: center;
    display: flex;
    flex-direction: column; 
    text-align: center; 
  }

  .inner-content {
    flex-direction: column;
    gap: 20px;
    align-items: center;
    width: 100%;
    text-align: center; 
  }

  .text-column {
    width: 100%;
    gap: 16px;
    align-items: center; 
    text-align: center; 
  }

  .small-title {
    font-size: 24px;
    line-height: 32px;
    width: 380px;
    text-align: center;
  }

  .large-title {
    font-size: 40px;
    line-height: 52px;
    width: 100%;
    text-align: center;
  }

  .description {
    font-size: 16px;
    line-height: 24px;
    width: 100%;
    text-align: center; 
  }

  .button-group {
    top: 40px;
    flex-direction: column;
    gap: 24px;
    align-items: center; 
  }

  .video {
    width: 80%;
    margin-top: 80px; 
  }

  .image-container {
    align-items: center;
    top: -20px;
  }

  .boostcamp-logo {
    width: 200px;
  }
}



</style>

<div class="frame">
  <div class="main-container">
    <Header />
    <div class="content">
      <div class="inner-content" name="생성하기">
        <div class="text-column">
          <div class="text-group">
            <div class="text-block">
              <div class="small-title">10초의 새로운 경험</div>
              <div class="large-title">내 목소리 다른 얼굴</div>
            </div>
            <div class="description">
              Introducing MZ team's new voice to face technology
              <br />
              where you can experience your own impressions and characters with
              your voice.
            </div>
          </div>
          <div class="button-group">
            <ButtonStyleFilled
              styleVariant="filled"
              style="background: #000000; border-color: #000000; flex-shrink: 0"
              name="나의 다른 모습 체험하기"
              targetPath="/login"
            />
            <ButtonStyleOutlined
              style="border-color: #000000; flex-shrink: 0"
              name="회원가입"
              targetPath="/join"
            />
          </div>
        </div>
        <div class="video">
          <video autoplay loop muted>
            <source src="{introVideo}" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      </div>
    </div>
    <div class="image-container">
      <img
        class="boostcamp-logo"
        src="/logo/boostcampLogo.jpg"
        alt="boostcamp"
      />
    </div>
  </div>
</div>