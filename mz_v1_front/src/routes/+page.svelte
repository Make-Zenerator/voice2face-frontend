<script>
    import ButtonStyleFilled from "./join/ButtonStyleFilled.svelte";
    import ButtonStyleOutlined from "./join/ButtonStyleOutlined.svelte";
    import PlaceholderImage from "./join/PlaceholderImage.svelte";
    import Header from "../components/header_non.svelte";
    let className = "";
    export { className as class };
    export let style;
  </script>
  <div
  style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 160px 0px; display: flex; flex-direction: column; gap: 160px; align-items: center; justify-content: flex-start; height: 849px; position: relative; ' + style}"
  >
  <Header/>
 <div>
    <div
      style="
        display: flex;
        flex-direction: column;
        gap: 64px;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        position: relative;
      "
      name="생성하기"
    >
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 40px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          width: 1216px;
          position: relative;
        "
      >
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 24px;
            align-items: flex-start;
            justify-content: flex-start;
            flex-shrink: 0;
            width: 612px;
            position: relative;
          "
        >
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 16px;
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
                gap: 8px;
                align-items: flex-start;
                justify-content: flex-start;
                flex-shrink: 0;
                position: relative;
              "
            >
              <div
                style="
                  color: #000000;
                  text-align: left;
                  font-family: var(
                    --title-small-font-family,
                    'DmSans-Bold',
                    sans-serif
                  );
                  font-size: var(--title-small-font-size, 32px);
                  line-height: var(--title-small-line-height, 40px);
                  font-weight: var(--title-small-font-weight, 700);
                  position: relative;
                  width: 612px;
                "
              >
                10초의 새로운 경험
              </div>
              <div
                style="
                  color: #000000;
                  text-align: left;
                  font-family: var(
                    --title-large-font-family,
                    'DmSans-Bold',
                    sans-serif
                  );
                  font-size: var(--title-large-font-size, 60px);
                  line-height: var(--title-large-line-height, 76px);
                  font-weight: var(--title-large-font-weight, 700);
                  position: relative;
                  width: 612px;
                "
              >
                내 목소리 다른 얼굴
              </div>
            </div>
            <div
              style="
                color: #8c8686;
                text-align: left;
                font-family: var(
                  --body-large-font-family,
                  'DmSans-Regular',
                  sans-serif
                );
                font-size: var(--body-large-font-size, 20px);
                line-height: var(--body-large-line-height, 32px);
                font-weight: var(--body-large-font-weight, 400);
                position: relative;
                width: 612px;
              "
            >
              Introducing MZ team&#039;s new voice to face technology
              <br />
              where you can experience your own impressions and characters with
              your voice.
            </div>
          </div>
          <div
            style="
              display: flex;
              flex-direction: row;
              gap: 24px;
              align-items: flex-start;
              justify-content: flex-start;
              flex-shrink: 0;
              position: relative;
            "
          >
            <ButtonStyleFilled
              styleVariant="filled"
              style="background: #000000; border-color: #000000; flex-shrink: 0"
              name="나의 다른 모습 체험하기"
              targetPath="/login"
            ></ButtonStyleFilled>
            <ButtonStyleOutlined
              style="border-color: #000000; flex-shrink: 0"
              name="회원가입"
              targetPath="/join"
            ></ButtonStyleOutlined>


          </div>
        </div>
        <PlaceholderImage
          style="align-self: stretch; flex: 1; height: auto"
        ></PlaceholderImage>
      </div>
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 20px;
          align-items: flex-start;
          justify-content: center;
          flex-shrink: 0;
          position: relative;
        "
      >
        <div
          style="
            color: #7e7676;
            text-align: left;
            font-family: var(
              --subtitle-small-font-family,
              'DmSans-Medium',
              sans-serif
            );
            font-size: var(--subtitle-small-font-size, 21px);
            line-height: var(--subtitle-small-line-height, 22px);
            font-weight: var(--subtitle-small-font-weight, 500);
            position: relative;
            width: 645px;
          "
        >
          Trusted by:
        </div>
        <div
          style="
            display: flex;
            flex-direction: row;
            gap: 64px;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            position: relative;
          "
        >
          <img
            class="group2"
            style="
              flex-shrink: 0;
              width: 120px;
              height: 39.31px;
              position: relative;
              overflow: visible;
            "
            src="/join/group1.svg"
            alt="youtube"
            
          />

          <img
            class="group3"
            style="
              flex-shrink: 0;
              width: 109.23px;
              height: 24.43px;
              position: relative;
              overflow: visible;
            "
            src="/join/group2.svg"
            alt="facebook"
          />
          
          <img
            class="frame"
            style="
              flex-shrink: 0;
              width: 135px;
              height: 31px;
              position: relative;
              overflow: visible;
            "
            src="/join/frame0.svg"
            alt="logo"
          />
        </div>
      </div>
    </div>
  </div>
  </div>