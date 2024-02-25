<script>
    import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
    import PlaceholderImage from "../aboutus_non/PlaceholderImage.svelte";
    import SocialProperty1Github from "../aboutus_non/SocialProperty1Github.svelte";
    let className = "";
    export { className as class };
    export let style;
  </script>
  <div
  style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 120px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
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
      <div
        style="
          color: var(--7b95b7, #6b6b6b);
          text-align: left;
          font-family: 'TitanOne-Regular', sans-serif;
          font-size: 24px;
          line-height: 24px;
          font-weight: 400;
          position: absolute;
          left: 188px;
          top: 31px;
        "
      >
        Make Zenerator
      </div>
      <img
        class="{'image-2 ' + className}"
        style="
          width: 90px;
          height: 55px;
          position: absolute;
          left: 98px;
          top: 8.5px;
          object-fit: cover;
        "
        src="/join/image-20.png"
      />
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
      <div
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
      </div>
      <div
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
        로그아웃
      </div>
      <ButtonStyleFilled
        styleVariant="filled"
        style="
          background: var(--6b6b6b, #000000);
          border-color: var(--7b95b7, #6b6b6b);
          flex-shrink: 0;
        "
        name="생성하기"
      ></ButtonStyleFilled>
    </div>
    </div>
    <div
      style="
        color: #000000;
        text-align: center;
        font-family: var(--title-large-font-family, 'DmSans-Bold', sans-serif);
        font-size: var(--title-large-font-size, 60px);
        line-height: var(--title-large-line-height, 76px);
        font-weight: var(--title-large-font-weight, 700);
        position: relative;
        width: 412px;
        height: 112px;
      "
    >
      About Us
    </div>
    <div
      style="
        color: #8c8686;
        text-align: center;
        font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
        font-size: var(--body-large-font-size, 20px);
        line-height: var(--body-large-line-height, 32px);
        font-weight: var(--body-large-font-weight, 400);
        position: relative;
        width: 612px;
      "
    >
      좋은 문구 생각나는 것 있으면 바로바로 적어주세유
    </div>
    <PlaceholderImage
      style="flex-shrink: 0; width: 769px; height: 392px"
    ></PlaceholderImage>
    <div
      style="
        display: flex;
        flex-direction: column;
        gap: 54px;
        align-items: center;
        justify-content: flex-start;
        flex-shrink: 0;
        position: relative;
      "
    >
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 81px;
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
            gap: 21px;
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
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              name
            </div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0"></SocialProperty1Github>
          <PlaceholderImage
            style="flex-shrink: 0; width: 343px; height: 343px"
          ></PlaceholderImage>
        </div>
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 21px;
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
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              name
            </div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0"></SocialProperty1Github>
          <PlaceholderImage
            style="flex-shrink: 0; width: 343px; height: 343px"
          ></PlaceholderImage>
        </div>
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 21px;
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
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              name
            </div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0"></SocialProperty1Github>
          <PlaceholderImage
            style="flex-shrink: 0; width: 343px; height: 343px"
          ></PlaceholderImage>
        </div>
      </div>
      <div
        style="
          display: flex;
          flex-direction: row;
          gap: 81px;
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
            gap: 21px;
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
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              name
            </div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0"></SocialProperty1Github>
          <PlaceholderImage
            style="flex-shrink: 0; width: 343px; height: 343px"
          ></PlaceholderImage>
        </div>
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 21px;
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
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              name
            </div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0"></SocialProperty1Github>
          <PlaceholderImage
            style="flex-shrink: 0; width: 343px; height: 343px"
          ></PlaceholderImage>
        </div>
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 21px;
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
              gap: 18px;
              align-items: flex-start;
              justify-content: flex-start;
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
                width: 294px;
                height: 40px;
              "
            >
              name
            </div>
          </div>
          <SocialProperty1Github style="flex-shrink: 0"></SocialProperty1Github>
          <PlaceholderImage
            style="flex-shrink: 0; width: 343px; height: 343px"
          ></PlaceholderImage>
        </div>
      </div>
    </div>
  </div>
  