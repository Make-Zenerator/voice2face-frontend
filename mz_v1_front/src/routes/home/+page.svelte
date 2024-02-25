<script>
    import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
    import ButtonStyleOutlined from "../join/ButtonStyleOutlined.svelte";
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
        padding: 32px 0px 0px 0px;
        display: flex;
        flex-direction: column;
        gap: 64px;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        position: relative;
      "
    >
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
                  --subtitle-large-font-family,
                  'DmSans-Medium',
                  sans-serif
                );
                font-size: var(--subtitle-large-font-size, 28px);
                line-height: var(--subtitle-large-line-height, 32px);
                font-weight: var(--subtitle-large-font-weight, 500);
                position: relative;
                align-self: stretch;
                display: flex;
                align-items: center;
                justify-content: center;
              "
            >
              무료로 경험하는
            </div>
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
            목소리를 통해 나의 또 다른 얼굴을
            <br />
            찾아보세요
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
            width: 196px;
            position: relative;
          "
        >
          <ButtonStyleFilled
            styleVariant="filled"
            style="
              background: var(--6b6b6b, #000000);
              border-color: var(--6b6b6b, #000000);
              flex-shrink: 0;
              width: 90px;
            "
            name="생성하기"
          ></ButtonStyleFilled>
          <ButtonStyleOutlined
            style="
              border-color: var(--6b6b6b, #000000);
              flex-shrink: 0;
              width: 90px;
            "
            name="결과확인"
          ></ButtonStyleOutlined>
        </div>
      </div>
      <div
        style="
          display: flex;
          flex-direction: column;
          gap: 20px;
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
            src="frame0.svg"
          />
        </div>
      </div>
    </div>
  </div>