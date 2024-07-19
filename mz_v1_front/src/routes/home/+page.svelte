<script>
  import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
  import ButtonStyleOutlined from "../join/ButtonStyleOutlined.svelte";
  import Header from "../../components/header/header_login.svelte"
</script>

<style>
  .frame { /* 전체 프레임 영역*/ 
    align-items: center;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    position: relative;
    overflow: hidden;
  }

  .main-container { /* 디자인 영역 */
    top: 160px;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 120px;
    padding: 0px 0px 120px 0px;
    position: relative;
    width:1200px;
    margin-bottom: 60px;
  }
  
  .text-container {
    padding: 32px 0px 0px 0px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .inner-text-group {
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
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
    color: var(--6b6b6b, #000000);
    text-align: center;
    font-family: var(--subtitle-large-font-family, 'DmSans-Medium', sans-serif);
    font-size: var(--subtitle-large-font-size, 28px);
    line-height: var(--subtitle-large-line-height, 32px);
    font-weight: var(--subtitle-large-font-weight, 500);
    align-self: stretch;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .text-style1 {
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
  }

  .text-style2 {
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
  }


  .button-row {
    display: flex;
    flex-direction: row;
    gap: 24px;
    align-items: flex-start;
    justify-content: center;
    flex-shrink: 0;
    width: 196px;
    position: relative;
  }

  .image-container {
    top: 30px;
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
    position: relative;
    overflow: visible;
    top: -50px;
  }


  @media(max-width: 420px) {
  .main-container {
    width: 100%;
    padding: 0px 16px 80px 16px;
    align-items: center;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .text-container {
    padding: 32px 0px 0px 0px;
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    width: 100%;
    text-align: center; /* 텍스트 중앙 정렬 */
  }

  .inner-text-group {
    display: flex;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
    width: 100%;
  }

  .text-block {
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--6b6b6b, #000000);
    text-align: center;
    font-family: var(--subtitle-large-font-family, 'DmSans-Medium', sans-serif);
    font-size: var(--subtitle-large-font-size, 24px);
    line-height: var(--subtitle-large-line-height, 28px);
    font-weight: var(--subtitle-large-font-weight, 500);
  }

  .text-style1 {
    color: var(--6b6b6b, #000000);
    text-align: center;
    font-family: var(--title-large-font-family, 'DmSans-Bold', sans-serif);
    font-size: var(--title-large-font-size, 40px);
    line-height: var(--title-large-line-height, 48px);
    font-weight: var(--title-large-font-weight, 700);
  }

  .text-style2 {
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 16px);
    line-height: var(--body-large-line-height, 24px);
    font-weight: var(--body-large-font-weight, 400);
    width: 100%;
  }

  .button-row {
    top: 40px;
    flex-direction: column;
    gap: 24px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 100%;
  }

  .image-container {
    top: 30px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    position: relative;
  }

  .boostcamp-logo {
    width: 200px;
    top: -30px;
  }
}


</style>
<div class="frame">
  <div class="main-container">
    <Header/>
    <div class="text-container">
      <div class="inner-text-group">
        <div class="text-block">
          <strong>무료로 경험하는</strong>
          <div class="text-style1">
            얼굴 생성하기
        </div>
        </div>
        <div class="text-block text-style2">
          목소리를 통해 나의 또 다른 얼굴을
          <br />
          찾아보세요
        </div>
      </div>
      <div class="button-row">
        <ButtonStyleFilled
          styleVariant="filled"
          style="
                background: var(--6b6b6b, #000000);
                border-color: var(--6b6b6b, #000000);
                flex-shrink: 0;
              "
          name="생성하기"
          targetPath="/infogather"
        ></ButtonStyleFilled>
        <ButtonStyleOutlined
          style="
              border-color: var(--6b6b6b, #000000);
              flex-shrink: 0;
            "
          name="결과확인"
          targetPath="/resultlist"
        ></ButtonStyleOutlined>
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