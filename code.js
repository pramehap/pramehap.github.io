function doGet(e) {
    return HtmlService.createTemplateFromFile('index')
      .evaluate()
      .setTitle('แบบฟอร์มจองห้องประชุม');
  }
  
  function submitFormData(data) {
    try {
      var sheet = SpreadsheetApp.openById("1V5W5JJMuPQyy6pqerd7saHh89HAeXUH6Tpfh52dpsQo/")
          .getSheetByName("Sheet1"); // เปลี่ยนชื่อชีตตามต้องการ
  
      sheet.appendRow([
        new Date(),
        data.name,
        data.department,
        data.phone,
        data.date1,
        data.date2,
        data.count,
        data.room
      ]);
  
      return {
        status: 'success',
        message: 'บันทึกข้อมูลสำเร็จ!'
      };
  
    } catch (error) {
      return {
        status: 'error',
        message: error.message
      };
    }
  }
  
  function include(filename) {
    return HtmlService.createTemplateFromFile(filename).getRawContent();
  }
