<script>
    import ButtonStyleFilled from "./join/ButtonStyleFilled.svelte";
    import ButtonStyleOutlined from "./join/ButtonStyleOutlined.svelte";
    import PlaceholderImage from "./join/PlaceholderImage.svelte";
    let className = "";
    export { className as class };
    export let style;
  </script>
  <div
    style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 160px 0px; display: flex; flex-direction: column; gap: 160px; align-items: center; justify-content: flex-start; height: 849px; position: relative; ' + style}"
  >
    <div
      style="
        background: var(--neutral-0, #ffffff);
        border-style: solid;
        border-color: var(--neutral-2, #dee5ed);
        border-width: 0px 0px 1px 0px;
        padding: 8px 98px 8px 98px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        flex-shrink: 0;
        width: 1440px;
        height: 72px;
        position: relative;
        overflow: hidden;
      "
    >
      <div style="flex-shrink: 0; width: 299px; height: 55px; position: static">
        <a href="/">
          <div
            style="
              color: var(--7b95b7, #6b6b6b);
              text-align: left;
              font-family: 'TitanOne-Regular', sans-serif;
              font-size: 24px;
              line-height: 24px;
              font-weight: 400;
              position: absolute;
              right: 72.43%;
              left: 13.06%;
              width: 14.51%;
              bottom: 23.24%;
              top: 42.96%;
              height: 33.8%;
            "
          >
            Make Zenerator
          </div>
          <img href="/"
            class="{'image-2 ' + className}"
            style="
              position: absolute;
              right: 86.94%;
              left: 6.81%;
              width: 6.25%;
              bottom: 11.27%;
              top: 11.27%;
              height: 77.46%;
              object-fit: cover;
            "
            src="/join/image-20.png"
            alt="logo"
          /></a>
      </div>
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 48px;
          align-items: center;
          justify-content: flex-start;
          flex-shrink: 0;
          position: relative;
        "
      >
        <a href="aboutus_non"
          style="
            color: var(--7b95b7, #6b6b6b);
            text-align: center;
            font-family: var(
              --body-small-font-family,
              'DmSans-Regular',
              sans-serif
            );
            font-size: var(--body-small-font-size, 16px);
            line-height: var(--body-small-line-height, 24px);
            font-weight: var(--body-small-font-weight, 400);
            position: relative;
          "
        >
          About us
    </a>
        <a href="/login"
          style="
            color: var(--7b95b7, #6b6b6b);
            text-align: center;
            font-family: var(
              --body-small-font-family,
              'DmSans-Regular',
              sans-serif
            );
            font-size: var(--body-small-font-size, 16px);
            line-height: var(--body-small-line-height, 24px);
            font-weight: var(--body-small-font-weight, 400);
            position: relative;
          "
        >
          로그인
  </a>
        <ButtonStyleFilled
          styleVariant="filled"
          style="
            background: var(--6b6b6b, #000000);
            border-color: var(--7b95b7, #6b6b6b);
            flex-shrink: 0;
            width: 96px;
          "
          name ="회원가입"
          targetPath="/join"
        ></ButtonStyleFilled>
      </div>
    </div>
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
          />
        </div>
      </div>
    </div>
  </div>