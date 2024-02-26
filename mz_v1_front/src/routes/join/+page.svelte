<script>
    import ButtonStyleFilled from "./ButtonStyleFilled.svelte";
    import RadioBigDefault from "./RadioBigDefault.svelte";
    import RadioSmallS from "./RadioSmallS.svelte";
    import PlaceholderImage from "./PlaceholderImage.svelte";
    import Header from "../../components/header_non.svelte";
    let className = "";
    let radioValue;
    export { className as class };
    export let style;
    let ageInput;

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
    console.log({ radioValue, ageInput });
    // 필요한 경우 여기에서 페이지 이동 로직을 추가합니다.
  }
  </script>
<!--  여기에 form 추가??-->

  <div
    style="{'background: var(--neutral-0, #ffffff);padding: 0px 0px 85px 0px; display: flex; flex-direction: column; gap: 99px; align-items: center; justify-content: flex-start; height: 1116px; position: relative; ' + style}"
  >
   <Header/>
    <div
      style="
        display: flex;
        flex-direction: row;
        gap: 41px;
        align-items: flex-start;
        justify-content: flex-start;
        flex-shrink: 0;
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
          flex-direction: row;
          align-items: flex-start;
          justify-content: center;
          flex-shrink: 0;
          width: 468px;
          height: 865px;
          position: relative;
          box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
          overflow: hidden;
        "
      >
        <div
          style="
            display: flex;
            flex-direction: column;
            gap: 43px;
            align-items: center;
            justify-content: flex-start;
            flex-shrink: 0;
            height: 822px;
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
            회원가입
          </div>
          <div
            style="
              display: flex;
              flex-direction: column;
              gap: 22px;
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
                gap: 13px;
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
                  gap: 10px;
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
                    font-family: 'DmSans-Medium', sans-serif;
                    font-size: 19px;
                    line-height: 40px;
                    font-weight: 500;
                    position: relative;
                    width: 125px;
                    height: 23px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                  "
                >
                  이메일 주소
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
                      width: 249px;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  >
                    이메일 입력
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
                    width: 125px;
                    height: 23px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                  "
                >
                  비밀번호
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
                      width: 250px;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  >
                    비밀번호 입력
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
                    width: 125px;
                    height: 23px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                  "
                >
                  비밀번호 확인
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
                      width: 252px;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  >
                    비밀번호 입력
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
                    width: 125px;
                    height: 23px;
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
                    position: relative;
                  "
                >
                  <RadioBigDefault
                    style="flex-shrink: 0; width: 137px"
                    name="남"
                  ></RadioBigDefault>
                  <RadioBigDefault
                    style="flex-shrink: 0; width: 100px"
                    name="여"
                  ></RadioBigDefault>
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
                    width: 125px;
                    height: 23px;
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
              </div>
              <div
                style="
                  display: flex;
                  flex-direction: column;
                  gap: 0px;
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
                    font-family: 'DmSans-Medium', sans-serif;
                    font-size: 20px;
                    line-height: 40px;
                    font-weight: 500;
                    position: relative;
                    width: 339px;
                    height: 43px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                  "
                >
                  개인정보 수집 이용 동의서
                </div>
                <div
                  style="
                    display: flex;
                    flex-direction: column;
                    gap: 5px;
                    align-items: flex-end;
                    justify-content: flex-start;
                    flex-shrink: 0;
                    position: relative;
                  "
                >
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
                      height: 158px;
                      position: relative;
                      overflow: hidden;
                    "
                  >
                    <div
                      style="
                        color: rgba(0, 0, 0, 0.4);
                        text-align: left;
                        font-family: 'DmSans-Medium', sans-serif;
                        font-size: 14px;
                        line-height: 40px;
                        font-weight: 500;
                        position: relative;
                        display: flex;
                        align-items: center;
                        justify-content: flex-start;
                      "
                    >
                      개인정보 어쩌고 저쩌고
                    </div>
                  </div>
                  <RadioSmallS style="flex-shrink: 0; width: 54px" name="동의"></RadioSmallS>
                </div>
              </div>
            </div>
            <ButtonStyleFilled
              styleVariant="filled"
              style="background: var(--7b95b7, #6b6b6b); flex-shrink: 0"
              name="회원가입"
            ></ButtonStyleFilled>
          </div>
        </div>
      </div>
      <PlaceholderImage
        style="flex-shrink: 0; width: 564px; height: 865px"
      ></PlaceholderImage>
    </div>
  </div>