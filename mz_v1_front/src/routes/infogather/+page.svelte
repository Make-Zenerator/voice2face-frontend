<script>
  import ButtonStyleFilled from "../join/ButtonStyleFilled.svelte";
  import RadioBigDefault from "../join/RadioBigDefault.svelte";
  import VoiceButtonDefaultVariant3 from "./VoiceButtonDefaultVariant3.svelte";
  import Frame7Default from "./Frame7Default.svelte";
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
      display: flex;
      flex-direction: row;
      gap: 82px;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      width: 1103px;
      height: 512px;
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
        height: 423px;
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
          height: 401px;
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
                <RadioBigDefault style="flex-shrink: 0" name="남"></RadioBigDefault>
                <RadioBigDefault style="flex-shrink: 0"name="여"></RadioBigDefault>
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
                justify-content: flex-start;
                flex-shrink: 0;
                width: 337px;
                height: 46px;
                position: relative;
                overflow: hidden;
              "
            >
              <div
                style="
                  color: rgba(0, 0, 0, 0.4);
                  text-align: center;
                  font-family: 'DmSans-Medium', sans-serif;
                  font-size: 14px;
                  line-height: 40px;
                  font-weight: 500;
                  position: relative;
                  width: 242px;
                  display: flex;
                  align-items: center;
                  justify-content: center;
                "
              >
                나이 입력
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
                align-items: flex-start;
                justify-content: center;
                flex-shrink: 0;
                width: 337px;
                position: relative;
              "
            >
              <VoiceButtonDefaultVariant3
                style="flex-shrink: 0"
              ></VoiceButtonDefaultVariant3>
              <Frame7Default style="flex-shrink: 0"></Frame7Default>
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
        <ButtonStyleFilled
          styleVariant="filled"
          style="
            background: var(--6b6b6b, #000000);
            border-color: var(--6b6b6b, #000000);
            flex-shrink: 0;
            width: 143px;
          "
          name="생성하기"
        ></ButtonStyleFilled>
      </div>
    </div>
  </div>
</div>
