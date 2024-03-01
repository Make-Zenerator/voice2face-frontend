<script>
    import ButtonStyleFilled from "../../components/button/join_filled.svelte";
    import PlaceholderImage from "./PlaceholderImage.svelte";
    import Header from "../../components/header_non.svelte";
    import Radio from "./radio.svelte"
    let className = "";
    let radioValue;
    export { className as class };
    export let style;
    let join_email;
    let join_pswd;
    let join_check;
    let join_gender;
    let join_age;
    let join_agree = false

    const options = [{
		value: 'Man',
		label: '남',
	},  {
		value: 'Woman',
		label: '여',
	}]
    const agree = [
      {
        value:'0',
        label:'동의 안함'
      },
      {
        value:'1', 
        label: '동의'
      },
  ]

  function handleSubmit(event) {
    event.preventDefault();
    // 여기에서 폼 데이터를 처리합니다. 예를 들어, 서버로 전송
    console.log({ radioValue, ageInput });
    alert("회원가입 완료했습니다. ")
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
          padding: 47px 0px 80px 0px;
          display: flex;
          flex-direction: row;
          align-items: flex-start;
          justify-content: center;
          flex-shrink: 0;
          width: 468px;

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
                  <input type='text' bind:value={join_email} placeholder="이메일 입력"
                    style="
                      color: rgba(0, 0, 0, 0.4);
                      text-align: center;
                      font-family: 'DmSans-Medium', sans-serif;
                      font-size: 14px;
                      line-height: 40px;
                      font-weight: 500;
                      position: relative;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  />
            
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
                  <input type='text' bind:value={join_pswd} placeholder="비밀번호 입력"
                    style="
                      color: rgba(0, 0, 0, 0.4);
                      text-align: center;
                      font-family: 'DmSans-Medium', sans-serif;
                      font-size: 14px;
                      line-height: 40px;
                      font-weight: 500;
                      position: relative;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                    "
                  />
                  
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
                  <input type='text' bind:value={join_check} placeholder="비밀번호 입력"
                    style="
                      color: rgba(0, 0, 0, 0.4);
                      text-align: center;
                      font-family: 'DmSans-Medium', sans-serif;
                      font-size: 14px;
                      line-height: 40px;
                      font-weight: 500;
                      position: relative;
                      width: 100%;
                      display: flex;
                      align-items: center;
                      justify-content: center;
                      margin: 0;
                      background: transparent;
                      -webkit-appearance: none;
                    "
                  />
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
                    align-items: center;
                  "
                >
                <Radio {options} fontSize={20} legend='' bind:userSelected={join_gender}/>
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
                <input
                type="number"
                bind:value="{join_age}"
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
                  <label style="display: flex; align-items: center; cursor: pointer;">
                    <input type="checkbox" bind:checked={join_agree}>
                    <span style="margin-left: 8px;">동의함</span>
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