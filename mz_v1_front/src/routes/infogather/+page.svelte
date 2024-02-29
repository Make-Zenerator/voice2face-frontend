<script>
  import ButtonStyleFilled from "./ButtonStyleFilled.svelte";
  import VoiceButtonDefaultVariant3 from "./VoiceButtonDefaultVariant3.svelte";
  import Frame7Default from "./Frame7Default.svelte";
  import Radio from "../join/radio.svelte";
  import Header from "../../components/header_login.svelte"
  let className = "";
  let info_gender;
  export { className as class };
  export let style;
  let info_age;

  const options = [{
		value: 'Man',
		label: '남',
	},  {
		value: 'Woman',
		label: '여',
	}]


  function handleSubmit(event) {
    event.preventDefault();
    // 여기에서 폼 데이터를 처리합니다. 예를 들어, 서버로 전송
    console.log({info_gender,info_age });
    alert('gender: ${info_gender} \n age: $:{info_age}')
    // 필요한 경우 여기에서 페이지 이동 로직을 추가합니다.
  }
</script>

<form on:submit|preventDefault={handleSubmit} style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 120px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}">
<div
  style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 120px 0px; display: flex; flex-direction: column; gap: 120px; align-items: center; justify-content: flex-start; height: 845px; position: relative; ' + style}"
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
          > <form method="POST">
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
    justify-content: center; /* 가운데 정렬 */
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
    min=0
    max=120
    style="
      color: rgba(0, 0, 0, 0.87);
      text-align: center;
      font-family: 'DmSans-Medium', sans-serif;
      font-size: 14px;
      line-height: 40px;
      font-weight: 500;
      border: none;
      width: 100%; /* 입력 상자가 div를 꽉 채우도록 조정 */
      height: 40px; /* 입력 상자의 높이 조정 */
      background: transparent; /* 배경색 투명 */
      -webkit-appearance: none; /* 스타일 초기화 */
      margin: 0; /* margin 초기화 */
    "

    placeholder="나이 입력" 
  />
</div> </form>

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
          targetPath="/loading"
        ></ButtonStyleFilled>
      </div>
    </div>
  </div>
</div>
</form>