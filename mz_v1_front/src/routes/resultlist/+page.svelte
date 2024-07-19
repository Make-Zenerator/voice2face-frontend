<script>
  import MovingFilled from "../../components/button/moving_filled.svelte";
  import Header from "../../components/header/header_login.svelte";
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  let className = "";
  export { className as class };
  export let style;
  import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';

  let items = [];

  const serverIP = import.meta.env.VITE_SERVER_IP;

  async function fetchData() {
    const token = sessionStorage.getItem('auth_token'); 

    const response = await fetch(`${serverIP}/api/v1/mz-request`, {
      method: 'GET',
      headers: {
        'Token': token,
      },
    });

    if (response.ok) {
      const data = await response.json();
      items = data.mz_request_list; 
    } else if(response.status === 400) {
      alert("데이터베이스 에러");
    } else if(response.status === 401) {
      alert(`세션이 만료되었습니다. \n다시 로그인 해주세요`);
      goto("/");
    }
    else {
      console.error('데이터를 가져오는 데 실패했습니다.');
      alert("요청 중 에러가 발생했습니다.");
    }
  }

  onMount(() => {
    fetchData(); 
    const interval = setInterval(fetchData, 5000); 

    return () => {
      clearInterval(interval); 
    };
  });
</script>

<style>
  .frame { 
    align-items: center;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    position: relative;
  }

  .main-container { 
    top: 120px;
    align-items: center;
    display: flex;
    flex-direction: column;
    gap: 80px;
    padding: 0px 0px 60px 0px;
    position: relative;
    width: 1200px;
    margin-bottom: 60px;
  }

  .img-container {
    display: flex;
    flex-direction: column;
    gap: 32px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    position: relative;
  }

  .logo {
    flex-shrink: 0;
    width: 150px;
    position: relative;
    object-fit: cover;
    margin-left: auto;
    margin-right: auto;
  }

  .description {
    color: #8c8686;
    text-align: center;
    font-family: var(--body-large-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-large-font-size, 20px);
    line-height: var(--body-large-line-height, 32px);
    font-weight: var(--body-large-font-weight, 400);
    position: relative;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
  }

  .table-frame {
    flex-shrink: 0;
    width: 70%;
    font-size: 14pt;
    position: relative;
    object-fit: cover;
    margin-left: auto;
    margin-right: auto;
  }

  .table-container {
    width: 100%;
    overflow-x: auto;
  }

  table {
    width: 100%;
    display: table;
    border-collapse: collapse;
  }

  th, td {
    white-space: nowrap;
  }

  .status-icon {
    width: 100%;
    height: 100%;
    max-width: 100%;
    max-height: 100%;
  }

  @media (max-width: 420px) {
    .frame { 
      align-items: center;
      background-color: #fff;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
      position: relative;
      width: 100%;
    }

    .main-container {
      top: 120px;
      width: 100%;
      padding: 0px 16px 60px 16px;
      align-items: center; 
      display: flex; 
      flex-direction: column; 
      margin-bottom: 30px;
    }

    .img-container {
      gap: 8px;
      width: 100%;
    }

    .description {
      font-size: 16px;
      line-height: 24px;
    }

    .table-frame {
      display: none;
    }

    .card-container {
      display: flex;
      overflow-x: scroll;
      padding: 16px;
    }

    .card {
      flex: 0 0 auto;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      margin-right: 16px;
      padding: 16px;
      width: 250px;
    }

    .card .card-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
    }

    .card .card-row:last-child {
      margin-bottom: 0;
    }

    .card .label {
      font-weight: bold;
    }
  }
</style>

<div class="frame">
  <div class="main-container">
    <Header />
    <div class="img-container">
      <img class="logo" src="./logo/logo1.png" alt="mz_logo" />
      <div class="description">
        생성 이미지는 선택 버튼을 통해 확인하실 수 있습니다.
      </div>
    </div>

    <div class="table-frame">
      <div class="table-container">
        <Table hoverable={true}>
          <TableHead>
            <TableHeadCell style="font-size:14pt; text-align: center;">요청 시간</TableHeadCell>
            <TableHeadCell style="font-size:14pt; text-align: center;">완료 시간</TableHeadCell>
            <TableHeadCell style="font-size:14pt; text-align: center;">성별</TableHeadCell>
            <TableHeadCell style="font-size:14pt; text-align: center;">나이</TableHeadCell>
            <TableHeadCell style="font-size:14pt; text-align: center;">Status</TableHeadCell>
            <TableHeadCell style="font-size:14pt; text-align: center;">Actions</TableHeadCell>
          </TableHead>
          <TableBody class="divide-y">
            {#each items as item}
              <TableBodyRow>
                <TableBodyCell>{item.created_at}</TableBodyCell>
                <TableBodyCell>
                  {#if item.updated_at != null} {item.updated_at}{/if}
                </TableBodyCell>
                <TableBodyCell>{item.gender}</TableBodyCell>
                <TableBodyCell>{item.age}</TableBodyCell>

                <TableBodyCell>
                  {#if item.status == null}
                    <img src="/resultlist/생성중.png" class="status-icon" alt="생성 중" />
                  {:else if item.status == "Success"}
                    <img src="/resultlist/생성완료.png" class="status-icon" alt="생성 완료" />
                  {:else}
                    <img src="/resultlist/생성실패.png" class="status-icon" style="height: 45%;" alt="생성 실패" />
                  {/if}
                </TableBodyCell>
                <TableBodyCell>
                  <audio src={item.voice_url} controls></audio>
                </TableBodyCell>
                <TableBodyCell>
                  {#if item.status == "Success"}
                    <MovingFilled targetPath='/result' name="결과 확인" id={item.id} latest_id={item.latest_mz_result_id} gender={item.gender}></MovingFilled>
                  {:else if item.status == "Failed"}
                    생성실패
                  {/if}
                </TableBodyCell>
              </TableBodyRow>
            {/each}
          </TableBody>
        </Table>
      </div>
    </div>

    <div class="card-container">
      {#each items as item}
        <div class="card">
          <div class="card-row">
            <span class="label">요청 시간:</span>
            <span>{item.created_at}</span>
          </div>
          <div class="card-row">
            <span class="label">완료 시간:</span>
            <span>{#if item.updated_at != null} {item.updated_at}{/if}</span>
          </div>
          <div class="card-row">
            <span class="label">성별:</span>
            <span>{item.gender}</span>
          </div>
          <div class="card-row">
            <span class="label">나이:</span>
            <span>{item.age}</span>
          </div>
          <div class="card-row">
            <span class="label">Status:</span>
            <span>
              {#if item.status == null}
                <img src="/resultlist/생성중.png" class="status-icon" alt="생성 중" />
              {:else if item.status == "Success"}
                <img src="/resultlist/생성완료.png" class="status-icon" alt="생성 완료" />
              {:else}
                <img src="/resultlist/생성실패.png" class="status-icon" style="height: 45%;" alt="생성 실패" />
              {/if}
            </span>
          </div>
          <div class="card-row">
            <audio src={item.voice_url} controls></audio>
          </div>
          <div class="card-row">
            {#if item.status == "Success"}
              <MovingFilled targetPath='/result' name="결과 확인" id={item.id} latest_id={item.latest_mz_result_id} gender={item.gender}></MovingFilled>
            {:else if item.status == "Failed"}
              생성실패
            {/if}
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>
