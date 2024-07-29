表格 1:

| 東森得易購股份有限公司東森購物平台建置專案系統設計報告書 |
| --- |
| 廠商及合作夥伴權限與選單維護 |
|  |
| 專案代號：東森購物平台建置專案文件代號：ETM2.0-SRM-廠商及合作夥伴權限與選單維護.docx版　　本：0.1日　　期：2024年1月24日撰　　寫：Andy Jin | 專案代號： | 東森購物平台建置專案 | 文件代號： | ETM2.0-SRM-廠商及合作夥伴權限與選單維護.docx | 版　　本： | 0.1 | 日　　期： | 2024年1月24日 | 撰　　寫： | Andy Jin |
| 專案代號： | 東森購物平台建置專案 |
| 文件代號： | ETM2.0-SRM-廠商及合作夥伴權限與選單維護.docx |
| 版　　本： | 0.1 |
| 日　　期： | 2024年1月24日 |
| 撰　　寫： | Andy Jin |

表格 2:

| 專案代號： | 東森購物平台建置專案 |
| --- | --- |
| 文件代號： | ETM2.0-SRM-廠商及合作夥伴權限與選單維護.docx |
| 版　　本： | 0.1 |
| 日　　期： | 2024年1月24日 |
| 撰　　寫： | Andy Jin |

表格 3:

| 變更記錄 |
| --- |
| 日期 | 作者 | 版本 | 摘要 |
| 2024/1/24 | Andy Jin | 0.1 | 初版 |
|  |  |  |  |

表格 4:

| 追蹤事項 |
| --- |
|  |

表格 5:

| 功能名稱 | 廠商及合作夥伴權限與選單維護 |
| --- | --- |
| 功能代號 | SRM-TX-0311 |
| 功能簡述 | 提供研發人員依照角色(包含一般廠商、特約商角色、外包倉角色等)設定B2B
選單權限，亦可依照特定廠商及合作夥伴設定B2B 選單權限。 |
| 進入功能路徑 | 供應商暨合作夥伴平台>廠商及合作夥伴帳號與權限維護>廠商及合作夥伴權限與選單維護 |
| 使用權限控管 | ■是 □否 |
| 使用審核流程 | □是 ■否 |
| 其他說明 |  |

表格 6:

| 權限角色選單TAB |
| --- |
|  |

表格 7:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
|  | 權限角色選單/廠商選單/合作夥伴選單 TAB |  | 文字 | 文字 | 依序顯示：權限角色選單、廠商選單、合作夥伴選單。預設在權限角色選單 TAB。 |
| 以下為查詢條件區塊 |
|  | 角色 | roles | string | 一般下拉選單 | 提示文字：請選擇。請參考動作與事件(角色)。 |
|  | 查詢 |  |  | 按鈕 | 請參考動作與事件(查詢)。 |
| 以上為查詢條件區塊 |
| 以下為功能按鈕區塊 |
|  | 新增權限角色 |  |  | 按鈕 | 請參考動作與事件「新增權限角色Pop-up」。 |
| 以上為功能按鈕區塊 |
| 以下為查詢結果區塊系統預設排序欄位：[modifiedDate](desc)，若是使用者選擇以其他欄位排序，將影響原系統預設排序結果。以sortable表示使用者可以決定該欄位遞增、遞減排序，未提及欄位表示系統不提供自行決定該欄位排序方式。以enable表示該欄位可編輯，未提及欄位表示不可編輯欄位內容。 |
|  | 群組名稱 | groupName | string | 文字 | 顯示：{ groupName }。sortable。 |
|  | 群組描述 | groupDescription | string | 文字 | 顯示：{ groupDescription }。sortable。 |
|  | 狀態 | status | string | SwitchBtn | 顯示：{ status }。enable。請參考動作與事件(狀態)。 |
|  | 最後異動人員 | modifiedBy | string | 文字 | 顯示：{ modifiedBy }。 |
|  | 最後異動時間 | modifiedDate | date | 文字 | 顯示：{ modifiedDate }。格式：yyyy/MM/dd HH:mm:ss。sortable。 |
|  | 操作 |  | icon | 按鈕 | 依序顯示：編輯icon、刪除icon。顯示編輯icon，請參考動作與事件(維護權限角色)。顯示刪除icon，點選後請參考動作與事件(刪除)。 |
| 以上為查詢結果區塊 |

表格 8:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 查詢 | click |  | 查詢條件：若為權限角色選單TAB，依[權限角色]查詢。若為廠商選單TAB，依[統一編號/身分證字號]+[廠商名稱]查詢。若為合作夥伴選單TAB，依[合作夥伴姓名]+[合作角色]查詢。 |  |
| 新增權限角色 | click |  | 點選後開啟「新增權限角色Pop-up」。 |  |
| 維護權限角色 | click |  | 點選後開啟「維護權限角色Pop-up」。 |  |
| 角色 | init |  | 呼叫「查詢角色清單」取得下拉選單資料。 |  |
| 狀態 | change |  | 呼叫「更新角色權限清單」更新資料。 |  |
| 刪除 | click |  | 呼叫「刪除角色權限資料」變更資料。 |  |

表格 9:

| 新增權限角色 (Pop-up) |
| --- |
|  |

表格 10:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
|  | 標題 |  | string | 文字 | 顯示文案：新增權限角色。 |
| 以下為權限角色選單資訊區塊以required表示該欄位必須有值，未提及欄位表示由使用者自行決定是否選取/輸入欄位值。 |
|  | 群組名稱 | groupName | string | 一般輸入框 | 提示文字：請輸入。required。限輸入最多15個中英文字。 |
|  | 群組描述 | groupDescription | string | 一般輸入框 | 提示文字：請輸入。required。限輸入最多15個中英文字。 |
|  | B2B功能選單 | 文字 | Checkbox | 輸入 | 必填。選項請參考 B2B功能清單。 |
| 以上為權限角色選單資訊區塊 |
| 以下為功能按鈕區塊 |
|  | 送出 |  |  | 按鈕 | 請參考動作與事件(送出)。 |
|  | 取消 |  |  | 按鈕 | 點選取消，關閉視窗回到原頁。 |
| 以上為功能按鈕區塊 |

表格 11:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 送出 | click |  | 呼叫「新增角色權限資料」新增一筆資料對應。送出新增至供應商平台若送出成功，則顯示成功 toast
訊息：已送出申請<換行>已成功送出選單新增。 |  |
| 取消 | click |  | 關閉視窗回到原頁。 |  |

表格 12:

| 維護權限角色 (Pop-up) |
| --- |
|  |

表格 13:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
|  | 標題 |  | 文字 | 文字 | 顯示文案：維護角色選單。 |
| 以下為權限角色選單資訊區塊以required表示該欄位必須有值，未提及欄位表示由使用者自行決定是否選取/輸入欄位值。以enable表示該欄位可編輯，未提及欄位表示不可編輯欄位內容。 |
|  | 群組名稱 | groupName | string | 一般輸入框 | required。enable。限輸入最多15個中英文字。 |
|  | 群組描述 | groupDescription | string | 一般輸入框 | required。enable。限輸入最多15個中英文字。 |
|  | B2B功能選單 |  | string | Checkbox | required。enable。請參考動作與事件(B2B功能選單)。 |
| 以上為權限角色選單資訊區塊 |
| 以下為功能按鈕區塊 |
|  | 送出 |  |  | 按鈕 | 請參考動作與事件(送出)。 |
|  | 取消 |  |  | 按鈕 | 點選取消，請參考動作與事件(取消)。 |
| 以上為功能按鈕區塊 |

表格 14:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 送出 | click |  | 呼叫「更新角色權限資料」更新資料對應。將資料存入DB若送出成功，則顯示成功toast訊息：已送出申請<換行>已成功送出選單新增。 |  |
| 取消 | click |  | 關閉視窗回到原頁。 |  |
| B2B功能選單 | init |  | 呼叫「查詢B2B功能選單」更新資料對應。 |  |

表格 15:

| 廠商選單TAB |
| --- |
|  |

表格 16:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
| 以下為查詢條件區塊 |
|  | 統一編號/身分證字號 | unifyNoOrIdNo | string |  | 提示文字：請輸入。選項：顯示所有{ unifyNoOrIdNo }。使用共用廠商編號查詢元件。 |
|  | 廠商編號/名稱 | supplierIdOrName | string |  | 提示文字：請輸入廠商編號或廠商名稱。使用共用廠商編號查詢元件。使用者選取後帶回並關閉選單。 |
|  | 查詢 |  |  | 按鈕 | 請參考功能說明(查詢)。 |
| 以上為查詢條件區塊 |
| 以下為查詢結果區塊系統預設排序欄位：[modifiedDate]
(desc)，若是使用者選擇以其他欄位排序，將影響原系統預設排序結果。以sortable表示使用者可以決定該欄位遞增、遞減排序，未提及欄位表示系統不提供自行決定該欄位排序方式。以enable表示該欄位可編輯，未提及欄位表示不可編輯欄位內容。 |
|  | 統一編號/身分證字號 | unifyNoOrIdNo | string |  | 提示文字：請輸入。選項：顯示所有{ unifyNoOrIdNo }。使用共用廠商編號查詢元件。 |
|  | 廠商編號 | supplierId | string |  | 提示文字：請輸入廠商編號或廠商名稱。使用共用廠商編號查詢元件。使用者選取後帶回並關閉選單。 |
|  | 廠商名稱 | supplierName | string | 文字 | 顯示：{supplierName}。 |
|  | 狀態 | stauts | string | SwitchBtn | 顯示：{ stauts }。enable。點選後啟用該廠商權限選單，並更新資料庫進行資料變動。 |
|  | 最後異動人員 | modifiedBy | string | 文字 | 顯示：{ modifiedBy }。 |
|  | 最後異動時間 | modifiedDate | date | 文字 | 顯示：{ modifiedDate }。格式：YYYY/MM/DD HH:mm:ss。sortable。 |
|  | 操作 |  | icon | 按鈕 | 依序顯示：編輯icon、刪除icon。顯示編輯icon，請參考動作與事件(維護權限角色)。顯示刪除icon，請參考動作與事件(刪除)。 |
| 以上為查詢結果區塊 |

表格 17:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 維護權限角色 | click |  | 點選後開啟「維護權限角色Pop-up」。 |  |
| 刪除 | click |  | 呼叫「刪除角色權限資料」變更資料。 |  |

表格 18:

| 維護廠商選單 (Pop-up) |
| --- |
|  |

表格 19:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
|  | 標題 |  | 文字 | 文字 | 顯示文案：維護廠商選單。 |
| 以下為廠商選單資訊區塊以required表示該欄位必須有值，未提及欄位表示由使用者自行決定是否選取/輸入欄位值。以enable表示該欄位可編輯，未提及欄位表示不可編輯欄位內容。 |
|  | 廠商編號 | supplierId | string | 文字 | 顯示：{ SupplierId }。 |
|  | 廠商名稱 | supplierName | string | 文字 | 顯示：{ supplierName }。 |
|  | B2B功能選單 |  | string | Checkbox | required。enable。選項請參考 B2B功能清單。 |
| 以上為廠商選單資訊區塊 |
| 以下為功能按鈕區塊 |
|  | 送出 |  |  | 按鈕 | 請參考動作與事件(送出)。 |
|  | 取消 |  |  | 按鈕 | 點選取消，請參考動作與事件(取消)。 |
| 以上為功能按鈕區塊 |

表格 20:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 送出 | click |  | 呼叫「更新角色權限資料」更新資料對應。若送出成功，則顯示成功toast訊息：已送出申請<換行>已成功送出選單新增。 |  |
| 取消 | click |  | 關閉視窗回到原頁。 |  |

表格 21:

| 合作夥伴選單TAB |
| --- |
|  |

表格 22:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
| 以下為查詢條件區塊 |
|  | 合作夥伴姓名 | partnerName | string |  | 提示文字：請輸入。限輸入最多15個中英文字。使用共用合作夥伴查詢元件。 |
|  | 合作角色 | collaborateRole | string | 一般下拉選單 | 提示文字：請選擇。選項：購物專家、直播主、藝人、團購主、來賓/見證、廠代。選項來源：[SRM_DOMAIN](DOMAINID:COLLABORATEROLE )。 |
|  | 查詢 | 文字 | 文字 | 按鈕 | 請參考功能說明(查詢)。 |
| 以上為查詢條件區塊 |
| 以下為查詢結果區塊系統預設排序欄位：[modifiedDate](desc)，若是使用者選擇以其他欄位排序，將影響原系統預設排序結果。以sortable表示使用者可以決定該欄位遞增、遞減排序，未提及欄位表示系統不提供自行決定該欄位排序方式。以enable表示該欄位可編輯，未提及欄位表示不可編輯欄位內容。 |
|  | 合作角色 | collaborateRole | 文字 | 文字 | 顯示：{ collaborateRole }。 |
|  | 合作夥伴姓名 | partnerName | 文字 | 文字 | 顯示：{ partnerName}。 |
|  | 狀態 | status | 文字 | SwitchBtn | 顯示：{ status }。enable。點選後啟用該合作夥伴權限選單，並更新資料庫進行資料變動。 |
|  | 最後異動人員 | modifiedBy | 文字 | 文字 | 顯示：{ modifiedBy }。 |
|  | 最後異動時間 | modifiedDate | 日期時間 | 文字 | 顯示：{ modifiedDate }。格式：yyyy/MM/dd HH:mm:ss。 |
|  | 操作 |  | icon | 按鈕 | 依序顯示：編輯icon、刪除icon。顯示編輯icon，請參考動作與事件(維護權限角色)。顯示刪除icon，請參考動作與事件(刪除)。 |
| 以上為查詢結果區塊 |

表格 23:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 維護權限角色 | click |  | 點選後開啟「維護權限角色Pop-up」。 |  |
| 刪除 | click |  | 呼叫「刪除角色權限資料」變更資料。 |  |

表格 24:

| 維護合作夥伴選單 (Pop-up) |
| --- |
|  |

表格 25:

| # | 中文欄位 | 英文欄位 | 資料型態 | 欄位型態 | 說明 |
| --- | --- | --- | --- | --- | --- |
|  | 標題 |  | 文字 | 文字 | 顯示文案：維護廠商選單。 |
| 以enable表示該欄位可編輯，未提及欄位表示不可編輯欄位內容。以required表示該欄位必須有值，未提及欄位表示由使用者自行決定是否選取/輸入欄位。 |
| 以下為合作夥伴選單資訊區塊 |
|  | 合作角色 | collaborateRole | 文字 | 文字 | 顯示：{ collaborateRole }。 |
|  | 合作夥伴姓名 | partnerName | 文字 | 文字 | 顯示：{ partnerName}。 |
|  | B2B功能選單 |  | 文字 | Checkbox | enable。required。選項請參考 B2B功能清單。 |
| 以上為合作夥伴選單資訊區塊 |
| 以下為功能按鈕區塊 |
|  | 送出 |  |  | 按鈕 | 請參考功能說明(送出)。 |
|  | 取消 |  |  | 按鈕 | 點選取消，請參考動作與事件(取消)。 |
| 以上為功能按鈕區塊 |

表格 26:

| 元件 | 動作 | 檢核 | 說明 | 錯誤處理 |
| --- | --- | --- | --- | --- |
| 送出 | click |  | 呼叫「更新角色權限資料」更新資料對應。若送出成功，則顯示成功toast訊息：已送出申請<換行>已成功送出選單更新。 |  |
| 取消 | click |  | 關閉視窗回到原頁。 |  |

表格 27:

| 基本資料 |
| --- |
| 功能說明 | 查詢角色清單 |
| 系統/提供者 | SRM / AP |
| 執行方式 | API |
| 設計規格 |
| API path | AccessRoleInfo/QueryAccessMenuRoles |
| 檢核邏輯 |  |
| 業務邏輯 | 呼叫AccessRoleInfoService方法QueryAccessMenuRoles取得角色清單關聯資料表：[SRM_ ACCESSROLESETTING]篩選條件：[STATUS]={true}回傳角色清單資料 |

表格 28:

| 基本資料 |
| --- |
| 功能說明 | 更新角色權限資料 |
| 系統/提供者 | SRM / AP |
| 執行方式 | API |
| 設計規格 |
| API path | AccessRoleInfo/UpdateAccessMenuRoles |
| 檢核邏輯 |  |
| 業務邏輯 | 呼叫AccessRoleInfoService方法UpdateAccessMenuRoles將前端form表單資料{AccessMenuRoles}帶入。更新設定table [SRM_ ACCESSROLESETTING]內容，{ GROUPNAME } = {
AccessMenuRoles.GroupName }{ GROUPDESCRIPTION }={ AccessMenuRoles.GroupDescription }{ STATUS }={ AccessMenuRoles.Status }更新權限關聯table[SRM_FUNCTIONMAPPING]，根據[FUNCTIONMAPPINGID]更新指定資料將[FUNCTIONMAPPINGID] = { AccessMenuRoles.
FunctionMappingId}資料全部刪除，並將{ AccessMenuRoles.Functions.IsCheck
} = 1新增一筆資料[B2BSYSTEMFUNCTIONCODE] = { b2bSystemFunctionCcode },[
B2BSYSTEMFUNCTIONCODE] = { b2bSystemFunctionCcode },{ GROUPID } = {
GroupId },{ COLLABORATENO } = { CollaborateNo
}進[SRM_FUNCTIONMAPPING]內。 |

表格 29:

| 基本資料 |
| --- |
| 功能說明 | 新增角色權限資料 |
| 系統/提供者 | SRM / AP |
| 執行方式 | API |
| 設計規格 |
| API path | AccessRoleInfo/CreateAccessMenuRoles |
| 檢核邏輯 |  |
| 業務邏輯 | 呼叫AccessRoleInfoService方法CreateAccessMenuRoles將前端form表單資料{AccessMenuRoles}帶入。新增設定table [SRM_ ACCESSROLESETTING]，[ GROUPNAME ] = {
AccessMenuRoles.GroupName }[ GROUPDESCRIPTION ]={ AccessMenuRoles.GroupDescription }[ STATUS ]={ AccessMenuRoles.Status }新增權限關聯table[SRM_FUNCTIONMAPPING]將{ AccessMenuRoles.Functions.IsCheck } = 1新增一筆資料[
B2BSYSTEMFUNCTIONCODE ] = { b2bSystemFunctionCcode },[
B2BSYSTEMFUNCTIONCODE ] = { b2bSystemFunctionCcode },[ GROUPID ] = {
GroupId },[ COLLABORATENO ] = { CollaborateNo
}進[SRM_FUNCTIONMAPPING]內。 |

表格 30:

| 基本資料 |
| --- |
| 功能說明 | 刪除角色權限資料 |
| 系統/提供者 | SRM / AP |
| 執行方式 | API |
| 設計規格 |
| API path | AccessRoleInfo/DeleteAccessMenuRoles |
| 檢核邏輯 |  |
| 業務邏輯 | 呼叫AccessRoleInfoService方法DeleteAccessMenuRoles將前端form表單資料{AccessMenuRoles.GroupId }帶入。將設定table [SRM_ ACCESSROLESETTING]，{ GROUPID } = {
AccessMenuRoles.GroupId }資料刪除。將權限關聯table[SRM_FUNCTIONMAPPING], { GROUPID } = {
AccessMenuRoles.GroupId }資料刪除。 |

表格 31:

| 基本資料 |
| --- |
| 功能說明 | 查詢B2B功能清單 |
| 系統/提供者 | SRM / AP |
| 執行方式 | API |
| 設計規格 |
| API path | SupplierMenu/QuerySupplierFunctions |
| 檢核邏輯 |  |
| 業務邏輯 | 呼叫SupplierMenuService方法QuerySupplierFunctions。帶入參數：{ CollaborateNo }、{ GroupId } or {空}。將查詢參數帶入[SRM_FUNCTIONMAPPING] 取得符合條件的資料[GROUPID] = { GroupId }[COLLABORATENO] = { CollaborateNo }將查詢結果[B2BSYSTEMFUNCTIONCODE] 紀錄。帶出所有[SRM_SYSTEMFUNCTION]內[STATUS]=1的資料。如果有設定的mapping資料{
B2bFunctionMapping.B2bSystemFunctionCodes }
與[SRM_SYSTEMFUNCTION]做結合,將重疊資料視為被選上的資料。 |

表格 32:

| 錯誤代碼 | 錯誤訊息 | 用意 | HTTP Status Code |
| --- | --- | --- | --- |
| SRM-0001 | 缺少必要欄位資訊 | API未接到必填欄位時 | 400 |

表格 33:

| PermissionCode | SystemFunctionCode | SystemCode | 說明 |
| --- | --- | --- | --- |
| SRM-TX-0311 | SRM-TX-0311 | SRM | 進入功能 |

表格 34:

| Field Name | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| COLLABORATIONNO | NUMBER(20) | TRUE | 關聯共用主檔編號 |
| COLLABORATIONCODE | NVARCHAR2(16) | TRUE | 關聯共用主檔類型代碼 |
| COLLABORATESTATUS | NUMBER(4,0) | TRUE | 合作狀態代碼(15) |
| DESCRIPTION | NVARCHAR2(512) | FALSE | 其它說明 |
| PAYMENTBANKNAME | NVARCHAR2(16) | FALSE | 請款銀行名稱 |
| PAYMENTBANKACCOUNT | NVARCHAR2(32) | FALSE | 請款銀行帳號 |
| CREATEDDATE | DATE | TRUE | 建立時間 |
| CREATEDBY | NVARCHAR2(16) | TRUE | 建立人員 |
|  |  |  |  |
| Field Name | Index state | Used columns | Index expression |
| SRM_COLLABORATION_PK | Primary Constraint | SRM_COLLABORATION.COLLABORATIONNO |  |

表格 35:

| Field Name | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| SUPPLIERID | NUMBER(20) | TRUE | 主檔流水號 |
| SUPIDENTIFYID | NVARCHAR2(16) | FALSE | 廠商識別碼 |
| COLLABORATIONNO | NVARCHAR2(16) | TRUE | 廠商編號 |
| UNIFYNO | NVARCHAR2(16) | FALSE | 統一編號 |
| IDNO | NVARCHAR2(16) | FALSE | 身分證字號 |
| SUPPLIERTYPE | NVARCHAR2(64) | TRUE | 供應商型態代碼(12) |
| MAINSTATUS | NVARCHAR2(64) | TRUE | 供應商主檔狀態代碼(54) |
| COLLABORATECHANNELTYPE | NVARCHAR2(64) | FALSE | 合作通路類別代碼(13) |
| SUPPLIERNAME | NVARCHAR2(16) | TRUE | 廠商名稱 |
| FULLNAME | NVARCHAR2(32) | TRUE | 供應商全名 |
| COMPANYTYPE | NVARCHAR2(16) | FALSE | 公司別代碼 |
| OVERSEASMALLTYPE | NVARCHAR2(64) | FALSE | 境外商城代碼(14) |
| CAPITALIZATION | NUMBER(10) | TRUE | 資本額 |
| ESTABLISHDATE | DATE | TRUE | 設立日期 |
| CONTACTAREACODE | NVARCHAR2(16) | TRUE | 聯絡區碼 |
| CONTACTNUMBER | NVARCHAR2(16) | TRUE | 聯絡電話 |
| CONTACTEXTENSION | NVARCHAR2(16) | FALSE | 聯絡分機 |
| FAXNUMBER | NVARCHAR2(16) | FALSE | 傳真號碼 |
| MANAGER | NVARCHAR2(16) | TRUE | 負責人 |
| RESEARCHABILITYTYPE | NVARCHAR2(64) | FALSE | 研發能力代碼(16) |
| NUMBEROFEMPLOYEE | NUMBER(7) | FALSE | 員工人數 |
| DEDUCTWHITELIST | NUMBER(1) | FALSE | 減量白名單 |
| ACCESSROLETYPE | NVARCHAR2(16) | FALSE | 權限角色代碼(21) |
| OPERATIONCODE | NVARCHAR2(64) | FALSE | 作業代碼 |
| PICKUPATSUPPLIERSHIPPINGCOMPANY | NVARCHAR2(16) | FALSE | 到廠取貨貨運商(一般情況) |
| DELIVERYDAYS | NUMBER(3) | FALSE | 配送天數 |
| ISSTOCKINGWHITELIST | NUMBER(1) | FALSE | 是否是入庫白名單 |
| RTNFACTORYPICKYN | NUMBER(1) | FALSE | 到廠逆物流 |
| INCOMEINVOICEFORMAT | NVARCHAR2(16) | FALSE | 進項發票格式 |
| CERTIFICATECODE | NVARCHAR2(16) | FALSE | 憑證代碼 |
| ISADVANCEPAY | NUMBER(1) | FALSE | 是否提前撥款 |
| ISAGENTINVOICE | NUMBER(1) | FALSE | 是否代開發票 |
| PAYMENTMETHODTYPE | NUMBER(4,0) | FALSE | 付款方式代碼(27) |
| TAXCODE | NVARCHAR2(16) | FALSE | 課稅代碼 |
| INSHOPSETTLECLASSTYPE | NUMBER(4,0) | FALSE | 店中店廠請代碼(29) |
| REQUESTPAYMENTREFUNDBASEDATETYPE | NUMBER(4,0) | FALSE | 廠請退款基準日代碼(30) |
| ISMARGINREQUIRED | NUMBER(1) | FALSE | 是否需繳保證金 |
| ISIDOFMANAGER | NUMBER(1) | TRUE | 是否可提供負責人身分證 |
| ISBUSINESSREGISTRATION | NUMBER(1) | TRUE | 是否可提供營業登記 |
| IS401REPORT | NUMBER(1) | TRUE | 是否可提供401表 |
| MD | NVARCHAR2(16) | FALSE | 指派商開 |
| CREATEDDATE | DATE | TRUE | 建立時間 |
| CREATEDBY | NVARCHAR2(16) | TRUE | 建立人員 |
|  |  |  |  |
| Field Name | Index state | Used columns | Index expression |
| SRM_SUPPLIER_PK | Primary Constraint | SRM_SUPPLIER.SUPPLIERID |  |

表格 36:

| Field Name | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| PARTNERID | NUMBER(20) | TRUE | 主檔流水號 |
| COLLABORATIONNO | NVARCHAR2(16) | TRUE | 廠商編號 |
| IDNO | NVARCHAR2(16) | FALSE | 身分證字號 |
| NAME | NVARCHAR2(16) | TRUE | 合作夥伴名稱 |
| ETMNO | NVARCHAR2(16) | FALSE | 東購編號 |
| MAINSTATUS | NUMBER(4,0) | TRUE | 合作夥伴主檔狀態代碼(54) |
| CONTACTPHONE | NVARCHAR2(16) | FALSE | 合作夥伴電話 |
| PARTNERBIRTHDAY | DATE | TRUE | 合作夥伴生日 |
| PARTNERNAME | NVARCHAR2(16) | TRUE | 合作夥伴姓名 |
| NUMBEROFEMPLOYEE | NUMBER(7) | FALSE | 直播主團隊人數 |
| CREATEDDATE | DATE | TRUE | 建立時間 |
| CREATEDBY | NVARCHAR2(16) | TRUE | 建立人員 |
|  |  |  |  |
| Field Name | Index state | Used columns | Index expression |
| SRM_PARTNER_PK | Primary Constraint | SRM_PARTNER.PARTNERID |  |

表格 37:

| Field Name | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| ACCESSROLESETTINGID | NUMBER(20) | TRUE | 群組ID |
| GROUPNAME | NVARCHAR2(16) | TRUE | 群組名稱 |
| GROUPDESCRIPTION | NVARCHAR2(256) | FALSE | 群組描述 |
| STATUS | NUMBER(1) | TRUE | 狀態 |
| MODIFIEDBY | NUMBER(6,0) | TRUE | 最後異動人員 |
| MODIFIEDDATE | DATE | TRUE | 最後異動時間 |
|  |  |  |  |
| Field Name | Index state | Used columns | Index expression |
| SRM_ACCESSROLESETTING_PK | Primary Constraint | SRM_ACCESSROLESETTING.ACCESSROLESETTINGID |  |

表格 38:

| Field Name | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| SYSTEMFUNCTIONCODE | NVARCHAR2(16) | TRUE | B2B功能代碼 |
| SYSTEMFUNCTIONNAME | NVARCHAR2(64) | TRUE | B2B功能名稱 |
| SYSTEMFUNCTIONPARENTCODE | NVARCHAR2(16) | FALSE | B2B母功能代碼 |
| ENTRYURL | NVARCHAR2(128) | FALSE | B2B功能連結 |
| SORT | NUMBER(3) | TRUE | B2B功能排序 |
| STATUS | NUMBER(1) | TRUE | 狀態 |
| MODIFIEDBY | NUMBER(6,0) | TRUE | 最後異動人員 |
| MODIFIEDDATE | DATE | TRUE | 最後異動時間 |
|  |  |  |  |
| Field Name | Index state | Used columns | Index expression |
| SRM_SYSTEMFUNCTION_PK | Primary Constraint | SRM_SYSTEMFUNCTION.SYSTEMFUNCTIONCODE |  |

表格 39:

| Field Name | Data Type | Mandatory | Description |
| --- | --- | --- | --- |
| FUNCTIONMAPPINGID | NUMBER(20) | TRUE | B2B功能Mapping檔流水號 |
| B2BSYSTEMFUNCTIONCODE | NVARCHAR2(16) | FALSE | B2B功能代碼 |
| GROUPID | NUMBER(20) | FALSE | 群組ID |
| COLLABORATENO | NVARCHAR2(16) | FALSE | 供應商編號 |
| MODIFIEDBY | NUMBER(6,0) | TRUE | 最後異動人員 |
| MODIFIEDDATE | DATE | TRUE | 最後異動時間 |
|  |  |  |  |
| Field Name | Index state | Used columns | Index expression |
| SRM_FUNCTIONMAPPING_PK | Primary Constraint | SRM_FUNCTIONMAPPING.FUNCTIONMAPPINGID |  |

