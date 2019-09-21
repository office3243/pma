
let inputDict ={
    "campaignName":"",
    "city":"",
    "locality":"",
    "subLocality":"",
    "category":"",
    "subCategory":"",
    "footerSize":"",
    "footerType":"",
    "footerFile":"",
    "logoFile":"",
    "brandName":"",
    "tagline":"",
    "info1":"",
    "info2":",",
    "extraImageFile":"",
    "quantity":"",
    "price":"",
    "footer":""
};
    let cDropdown = document.querySelector('#city');
    let cDefaultOption = document.createElement('option');
        cDefaultOption.text = 'Choose City...';
        cDefaultOption.value = '';
        cDropdown.add(cDefaultOption);
        cDropdown.selectedIndex = 0;
    let cOption;
    for(let i=0;i< city.length;i++){
        cOption = document.createElement('option');
        cOption.text = city[i].name;
        cDropdown.add(cOption);
    }
    function addLocality(element){
        removeInvalidClass(element);
        let cityVal = document.querySelector("#city").value;
        let lDropdown = document.querySelector("#locality");
        let l = lDropdown.length;
        for(let i=0;i<l;i++){
            lDropdown.remove(0);
        }
        let lDefaultOption = document.createElement('option');
        lDefaultOption.text = "Choose City First...";
        lDefaultOption.value = "";
        lDropdown.add(lDefaultOption);
        lDropdown.selectedIndex = 0;
        let lDropdown2 = document.querySelector("#subLocality");
        let l2 = lDropdown2.length;
        for(let i=0;i<l2;i++){
            lDropdown2.remove(0);
        }
        let lDefaultOption2 = document.createElement('option');
        lDefaultOption2.text = "Choose Locality First...";
        lDefaultOption2.value = "";
        lDropdown2.add(lDefaultOption2);
        lDropdown2.selectedIndex = 0;
        let lOption,i;
        for(i=0;i<city.length;i++){
            if(city[i].name == cityVal){
                break;
            }
        }
        if(i< city.length){
            lDefaultOption.text = "Choose Locality...";
            lDefaultOption.value = "";
            for(let j=0;j<city[i].locality.length;j++){
                lOption = document.createElement('option');
                lOption.text = city[i].locality[j].name;
                lDropdown.add(lOption);
            }
        }
    }
    function addSubLocality(element){
        removeInvalidClass(element);
        let cityVal = document.querySelector("#city").value;
        let localityVal = document.querySelector("#locality").value;
        let lDropdown = document.querySelector("#subLocality");
        let l = lDropdown.length;
        for(let i=0;i<l;i++){
            lDropdown.remove(0);
        }
        let lDefaultOption = document.createElement('option');
        lDefaultOption.text = "Choose Locality First...";
        lDefaultOption.value = "";
        lDropdown.add(lDefaultOption);
        lDropdown.selectedIndex = 0;
        let lOption,i,j;
        for(i=0;i<city.length;i++){
            if(city[i].name == cityVal){
                break;
            }
        }
        for(j=0;j<city[i].locality.length;j++){
            if(city[i].locality[j].name == localityVal){
                break;
            }
        }
        if(j< city[i].locality.length){
            lDefaultOption.text = "Choose Sub Locality...";
            lDefaultOption.value = "";
            for(let k=0;k<city[i].locality[j].subLocality.length;k++){
                lOption = document.createElement('option');
                lOption.text = city[i].locality[j].subLocality[k].name;
                lDropdown.add(lOption);
            }
        }
    }

    let caDropdown = document.querySelector('#category');
    let caDefaultOption = document.createElement('option');
        caDefaultOption.text = 'Choose Category...';
        caDefaultOption.value = '';
        caDropdown.add(caDefaultOption);
        caDropdown.selectedIndex = 0;
    let caOption;
    for(let i=0;i< category.length;i++){
        caOption = document.createElement('option');
        caOption.text = category[i].name;
        caDropdown.add(caOption);
    }
    function addSubCategory(element){
        removeInvalidClass(element);
        let categoryVal = document.querySelector("#category").value;
        let sDropdown = document.querySelector("#subCategory");
        let l = sDropdown.length;
        for(let i=0;i<l;i++){
            sDropdown.remove(0);
        }
        let sDefaultOption = document.createElement('option');
        sDefaultOption.text = "Choose Category First...";
        sDefaultOption.value = "";
        sDropdown.add(sDefaultOption);
        sDropdown.selectedIndex = 0;
        let sOption,i;
        for(i=0;i<category.length;i++){
            if(category[i].name == categoryVal){
                break;
            }
        }
        if(i< category.length){
            sDefaultOption.text = "Choose SubCategory...";
            sDefaultOption.value = "";
            for(let j=0;j<category[i].subCategory.length;j++){
                sOption = document.createElement('option');
                sOption.text = category[i].subCategory[j].name;
                sDropdown.add(sOption);
            }
        }
    }

    // let fDropdown = document.querySelector('#footerSize');
    // let fDefaultOption = document.createElement('option');
    //     fDefaultOption.text = 'Choose Size of Footer...';
    //     fDefaultOption.value = '';
    //     fDropdown.add(fDefaultOption);
    //     fDropdown.selectedIndex = 0;
    // let fOption;
    // for(let i=0;i< footerSizeRate.length;i++){
    //     fOption = document.createElement('option');
    //     fOption.text = footerSizeRate[i].size + " cm ( Rate: " + footerSizeRate[i].rate + " per Footer )";
    //     fOption.value = footerSizeRate[i].rate;
    //     fDropdown.add(fOption);
    // }
    let fDropdown = document.querySelector('#footerSize');
    let fDefaultOption = document.createElement('option');
        fDefaultOption.text = 'Choose Size of Footer...';
        fDefaultOption.value = '';
        fDropdown.add(fDefaultOption);
        fDropdown.selectedIndex = 0;
    let fOption;
    for(let i=0;i< footerSizeRate.length;i++){
        fOption = document.createElement('option');
        fOption.text = footerSizeRate[i].size + " cm ( Rate: " + footerSizeRate[i].rate + " per Footer )";
        fOption.value = footerSizeRate[i].no;
        fDropdown.add(fOption);
    }

    let qDropdown = document.querySelector('#quantity');
    let qDefaultOption = document.createElement('option');
        qDefaultOption.text = 'Choose Quantity...';
        qDefaultOption.value = '';
        qDropdown.add(qDefaultOption);
        qDropdown.selectedIndex = 0;
    let qOption;
    for(let i=0;i< quantity.length;i++){
        qOption = document.createElement('option');
        qOption.text = quantity[i].value + " ( Rate: " + quantity[i].rate + " per Footer )";
        qOption.value = quantity[i].rate;
        qDropdown.add(qOption);
    }
    function showFooterPreview(footerValue){
        for(let i=1;i<=7;i++)
            $('#footerContainer'+i).hide();
        $('#footerPreviewDiv').show();
        if(footerValue == 1)
            $('#footerContainer1').show();
        else if(footerValue == 2)
            $('#footerContainer2').show();
        else if(footerValue == 3)
            $('#footerContainer3').show();
        else if(footerValue == 4)
            $('#footerContainer4').show();
        else if(footerValue == 5)
            $('#footerContainer5').show();
        else if(footerValue == 6)
            $('#footerContainer6').show();
        else if(footerValue == 7)
            $('#footerContainer7').show();
        else
            $('#footerPreviewDiv').hide();
    }
    function setFooterPreviewDefault(){
        document.getElementById('logoFile').value = "";
        logoFileChange();
        document.getElementById('BrandName').value = "";
        document.getElementById('Tagline').value = "";
        document.getElementById('Info1').value = "";
        document.getElementById('Info2').value = "";
        document.getElementById('extraImage').value = "";
        extraImageChange();
        document.getElementById('footerColor').value = "#ffffff";
        colorChange(document.getElementById('footerColor'),'lblFooterColor','BC');
        document.getElementById('fontColor').value = "#000000";
        colorChange(document.getElementById('fontColor'),'lblFontColor','FC');
        for(i=1;i<=7;i++){
            document.getElementById('footerContainer'+i).style.background = "#fff";
            document.getElementById('footerContainer'+i).style.color = "#000";
            document.getElementById('fLogoImg'+i).src = "/Default Logo.png";
            if(i>1){
                document.getElementById('fBrandName'+i).innerHTML = "Brand Name";
                if(i>2){
                    document.getElementById('fInfo1'+i).innerHTML = "Info1";
                    if(i>3){
                        document.getElementById('fInfo2'+i).innerHTML = "Info2";
                        if(i>4){
                            document.getElementById('fTagline'+i).innerHTML = "Tagline";
                            if(i>5){
                                document.getElementById('fExtraImg'+i).src = "/noimages.png";
                            }
                        }
                    }
                }
            }
        }
        let size=document.querySelector('#footerSize').value;
        if(size == 2){
            fontChange(document.getElementById('bf4'),'fBrandName');
        }else if(size == 3){
            fontChange(document.getElementById('bf6'),'fBrandName');
            infoFontChange(document.getElementById('if3'));
        }else if(size >= 4){
            fontChange(document.getElementById('bf6'),'fBrandName');
            infoFontChange(document.getElementById('if2'));
            if(size > 4)
                fontChange(document.getElementById('tf4'),'fTagline');

        }
    }
    function footerSizeChange(element){
        removeInvalidClass(element);
        calculatePrice();
        setFooterPreviewDefault();
        let footerValue = element.value;
        showFooterPreview(footerValue);
        if(footerValue > 1){
            document.querySelector('#divBrandName').style.display = "block";
            document.querySelector('#colorBlock').style.display = "block";
            if(footerValue > 2){
                document.querySelector('#divInfo1').style.display = "block";
                document.querySelector('#divInfoFont').style.display = "block";
                if(footerValue > 3){
                    document.querySelector('#divInfo2').style.display = "block";
                    if(footerValue > 4){
                        document.querySelector('#divTagline').style.display = "block";
                        if(footerValue > 5){
                            document.querySelector('#divExtraImage').style.display = "block";
                        }else{
                            document.querySelector('#divExtraImage').style.display = "none";
                        }
                    }else{
                        document.querySelector('#divTagline').style.display = "none";
                        document.querySelector('#divExtraImage').style.display = "none";
                    }
                }else{
                    document.querySelector('#divInfo2').style.display = "none";
                    document.querySelector('#divTagline').style.display = "none";
                    document.querySelector('#divExtraImage').style.display = "none";
                }
            }else{
                document.querySelector('#divInfo1').style.display = "none";
                document.querySelector('#divInfoFont').style.display = "none";
                document.querySelector('#divInfo2').style.display = "none";
                document.querySelector('#divTagline').style.display = "none";
                document.querySelector('#divExtraImage').style.display = "none";
            }
        }else{
            document.querySelector('#divBrandName').style.display = "none";
            document.querySelector('#colorBlock').style.display = "none";
            document.querySelector('#divInfo1').style.display = "none";
            document.querySelector('#divInfoFont').style.display = "none";
            document.querySelector('#divInfo2').style.display = "none";
            document.querySelector('#divTagline').style.display = "none";
            document.querySelector('#divExtraImage').style.display = "none";
        }
    }
    function quantityCalculate(element){
        removeInvalidClass(element);
        calculatePrice();
    }
    function calculatePrice(){
       let footerno = document.querySelector('#footerSize').value;
       let footerRate;
       for(let i=0;i<footerSizeRate.length;i++){
           if(footerno == footerSizeRate[i].no)
                footerRate = footerSizeRate[i].rate;
       }
       let quantityRate = document.querySelector('#quantity').value;
       let quantityValue;
       for(let i=0;i<quantity.length;i++){
            if(quantityRate == quantity[i].rate){
                quantityValue = quantity[i].value;
            }
       }
       if(quantityRate != "" && footerno != ""){
            document.querySelector('#price').innerHTML = quantityValue*quantityRate*footerRate;
       }else {
        document.querySelector('#price').innerHTML = 0;
       }
    }

    function showFooterForm(){
        document.querySelector('#footerType').classList.remove("is-invalid");
        let footerType1 = document.getElementById('footerType1').checked;
        if(footerType1 == true){
            document.querySelector('#footerTypeDiv1').style.display = "block";
            document.querySelector('#footerTypeDiv2').style.display = "none";
            // document.querySelector('#pfooterContainer7').style.display = "block";
            // document.querySelector('#footerContainer7').style.display = "none";
        }
        else{
            document.querySelector('#footerTypeDiv2').style.display = "block";
            document.querySelector('#footerTypeDiv1').style.display = "none";
            // document.querySelector('#footerContainer7').style.display = "block";
            // document.querySelector('#pfooterContainer7').style.display = "none";
        }
    }

    function footerFileChange(){
        let footerFile = document.querySelector('#footerFile');
        if(footerFile.files.length != 0){
            document.querySelector('#lblFooterFile').classList.remove("is-invalid");
            document.querySelector('#footerFileSpan').innerHTML= footerFile.files[0].name;
        }else{
            document.querySelector('#footerFileSpan').innerHTML = "Upload File";
        }
    }

    function logoFileChange(){
        let logoFile = document.querySelector('#logoFile');
        let size = document.querySelector('#footerSize').value;
        if(logoFile.files.length != 0){
            document.querySelector('#lblLogoFile').classList.remove("is-invalid");
            document.querySelector('#logoFileSpan').innerHTML= logoFile.files[0].name;
            var reader = new FileReader();
            reader.onload = function (e) {
               $('#fLogoImg'+size).attr('src', e.target.result);
            }
           reader.readAsDataURL(logoFile.files[0]);
        }else{
            document.querySelector('#logoFileSpan').innerHTML = "Upload Logo";
        }
    }
    function nameChange(id){
        let element = document.getElementById(id);
        let size = document.querySelector('#footerSize').value;
        removeInvalidClass(element);
        document.getElementById("f"+id+size).innerHTML = element.value;
    }
    function infoFontChange(element){
        let size = document.querySelector('#footerSize').value;
        if(size == 3){
            fontChange(element,"fInfo1");
        }else if(size > 3){
            fontChange(element,"fInfo1");
            fontChange(element,"fInfo2");
        }

    }
    function fontChange(element,id){
        let lid = "l" + element.id.slice(0,-1);
        for(let i=1;i<=6;i++){
            if(document.getElementById(lid + i).classList.contains("tz-fontSize-Label-active")){
                document.getElementById(lid + i).classList.remove("tz-fontSize-Label-active");
            }
        }
        document.getElementById("l" + element.id).classList.add("tz-fontSize-Label-active");
        let clss = "tz-footer-fontSize-",
        size = document.querySelector('#footerSize').value;
        id = document.getElementById(id+size);
        for(let i=1;i<=6;i++){
            if(id.classList.contains(clss+i)){
                id.classList.remove(clss+i);
            }
        }
        id.classList.add(clss+element.value);
    }
    function extraImageChange(){
        let extraImage = document.querySelector('#extraImage');
        let size = document.querySelector('#footerSize').value;
        if(extraImage.files.length != 0){
            document.querySelector('#lblExtraImage').classList.remove("is-invalid");
            document.querySelector('#extraImageSpan').innerHTML= extraImage.files[0].name;
            var reader = new FileReader();
            reader.onload = function (e) {
               $('#fExtraImg'+size).attr('src', e.target.result);
            }
           reader.readAsDataURL(extraImage.files[0]);
        }else{
            document.querySelector('#extraImageSpan').innerHTML = "Upload Extra Image";
        }
    }
    function colorChange(element,id,cType){
        let color = element.value;
        document.getElementById(id).style.background = color;
        let size = document.querySelector('#footerSize').value;
        if(cType == 'BC'){
            document.getElementById('footerContainer'+size).style.background = color;
        }else{
            document.getElementById('footerContainer'+size).style.color = color;
        }
    }
    function showDict(){
        let campaignName = document.querySelector('#campaignName').value;
        let city = document.querySelector('#city').value;
        let locality = document.querySelector('#locality').value;
        let subLocality = document.querySelector('#subLocality').value;
        let category = document.querySelector('#category').value;
        let subCategory = document.querySelector('#subCategory').value;
        let footerVal = document.querySelector('#footerSize').value;
        let footerType1 = document.querySelector('#footerType1').checked;
        let footerType2 = document.querySelector('#footerType2').checked;
        let footerFile = document.querySelector('#footerFile');
        let logoFile = document.querySelector('#logoFile');
        let brandName = document.querySelector('#BrandName').value;
        let tagline = document.querySelector('#Tagline').value;
        let info1 = document.querySelector('#Info1').value;
        let info2 = document.querySelector('#Info2').value;
        let extraImageFile = document.querySelector('#extraImage');
        let quantityRate = document.querySelector('#quantity').value;
        let price = document.querySelector('#price').innerHTML;
        if(campaignName != ""){
            inputDict.campaignName = campaignName;
        }else{
            inputDict.campaignName = "";
        }
        if(city != ""){
            inputDict.city = city;
        }else{
            inputDict.city = "";
        }
        if(locality != ""){
            inputDict.locality = locality;
        }else{
            inputDict.locality = "";
        }
        if(subLocality != ""){
            inputDict.subLocality = subLocality;
        }else{
            inputDict.subLocality = "";
        }
        if(category != ""){
            inputDict.category = category;
        }else{
            inputDict.category = "";
        }
        if(subCategory != ""){
            inputDict.subCategory = subCategory;
        }else{
            inputDict.subCategory = "";
        }
        if(footerVal != ""){
            for(let i=0; i<footerSizeRate.length; i++){
                if(footerSizeRate[i].no == footerVal){
                    inputDict.footerSize = footerSizeRate[i].size;
                }
            }
        }else{
            inputDict.footerSize = "";
        }
        if(footerType1){
            inputDict.footerType = "UPLOAD FOOTER";
        }else if(footerType2){
            inputDict.footerType = "GENERATE FOOTER";
        }else{
            inputDict.footerType = "";
        }
        if(footerFile.files.length == 1){
            inputDict.footerFile = footerFile.files[0];
        }else{
           inputDict.footerFile = "";
       }
       if(logoFile.files.length == 1){
            inputDict.logoFile = logoFile.files[0];
        }else{
            inputDict.logoFile = "";
        }
        if(brandName != ""){
            inputDict.brandName = brandName;
        }else{
            inputDict.brandName = "";
        }
        if(tagline != ""){
            inputDict.tagline = tagline;
        }else{
            inputDict.tagline = "";
        }
        if(info1 != ""){
            inputDict.info1 = info1;
        }else{
            inputDict.info1 = "";
        }
        if(info2 != ""){
            inputDict.info2 = info2;
        }else{
            inputDict.info2 = "";
        }
        if(extraImageFile.files.length == 1){
            inputDict.extraImageFile = extraImageFile.files[0];
        }else{
            inputDict.extraImageFile = "";
        }
        if(quantityRate != ""){
            for(let i=0; i<quantity.length; i++){
                if(quantity[i].rate == quantityRate){
                    inputDict.quantity = quantity[i].value;
                }
            }
        }else{
            inputDict.quantity = "";
        }
        if(quantityRate != "" && footerVal != ""){
            inputDict.price = price
        }else{
            inputDict.price = ""
        }

    //    console.log(inputDict);

    }
    function removeInvalidClass(element){
        if(element.value != ""){
            element.classList.remove("is-invalid");
        }else{
            element.classList.add("is-invalid");
        }
    }
    function goToStep1(){
        document.querySelector('#campaignForm1').style.display = "block";
        document.querySelector('#campaignForm2').style.display = "none";
    }
    function goToStep2(){
        let campaignName = document.querySelector('#campaignName').value;
        let city = document.querySelector('#city').value;
        let locality = document.querySelector('#locality').value;
        let subLocality = document.querySelector('#subLocality').value;
        let category = document.querySelector('#category').value;
        let subCategory = document.querySelector('#subCategory').value;
        if(campaignName != "" && city != "" && locality != "" && subLocality != "" && category != "" && subCategory != ""){
            document.querySelector('#campaignForm2').style.display = "block";
            document.querySelector('#campaignForm1').style.display = "none";
            document.querySelector('#campaignForm3').style.display = "none";
        }else{
            if(campaignName == ""){
                document.querySelector('#campaignName').classList.add("is-invalid");
            }
            if(city == ""){
                document.querySelector('#city').classList.add("is-invalid");
            }
            if(locality == ""){
                document.querySelector('#locality').classList.add("is-invalid");
            }
            if(subLocality == ""){
                document.querySelector('#subLocality').classList.add("is-invalid");
            }
            if(category == ""){
                document.querySelector('#category').classList.add("is-invalid");
            }
            if(subCategory == ""){
                document.querySelector('#subCategory').classList.add("is-invalid");
            }
        }
    }
    function goToStep3(){
        let footerSize = document.querySelector('#footerSize');
        let footerType1 = document.querySelector('#footerType1');
        let footerType2 = document.querySelector('#footerType2');
        let footerFile = document.querySelector('#footerFile');
        let logoFile = document.querySelector('#logoFile');
        let brandName = document.querySelector('#BrandName');
        let tagline = document.querySelector('#Tagline');
        let info1 = document.querySelector('#Info1');
        let info2 = document.querySelector('#Info2');
        let extraImage = document.querySelector('#extraImage');

        if(footerSize.value != "" && footerType1.checked == true && footerFile.files.length == 1){
            document.querySelector('#campaignForm3').style.display = "block";
            document.querySelector('#campaignForm4').style.display = "none";
            document.querySelector('#campaignForm2').style.display = "none";
            logoFile.value = "";
            document.querySelector('#logoFileSpan').innerHTML = "Upload Logo";
            brandName.value = "";
            tagline.value = "";
            info1.value = "";
            info2.value = "";
            extraImage.value = "";
            document.querySelector('#extraImageSpan').innerHTML = "Upload Image";
        }else if(footerSize.value != "" && footerType2.checked == true){
            let size = footerSize.value;
            if(size == 1 && logoFile.files.length == 1){
                html2canvas(document.querySelector('#footerContainer'+size),{
                    onrendered: function(canvas){
                        let imgFooter = canvas.toDataURL('image/png');
                        let doc = new jsPDF('P','mm','a4');
                        let width = 28;
                        let height = 10;
                        doc.addImage(imgFooter,'PNG',3,3,width,height);
                        // doc.save('Test.pdf');
                        inputDict.footer = doc.output('blob');
                        document.querySelector('#campaignForm3').style.display = "block";
                        document.querySelector('#campaignForm4').style.display = "none";
                        document.querySelector('#campaignForm2').style.display = "none";
                        footerFile.value = "";
                        document.querySelector('#footerFileSpan').innerHTML = "Upload File";
                        brandName.value = "";
                        info1.value = "";
                        info2.value = "";
                        tagline.value = "";
                        extraImage.value = "";
                        document.querySelector('#extraImageSpan').innerHTML = "Upload Image";
                    }
                });
            }else if(size == 2 && logoFile.files.length == 1 && brandName.value != ""){
                html2canvas(document.querySelector('#footerContainer'+size),{
                    onrendered: function(canvas){
                        let imgFooter = canvas.toDataURL('image/png');
                        let doc = new jsPDF('P','mm','a4');
                        let width = 56;
                        let height = 10;
                        doc.addImage(imgFooter,'PNG',3,3,width,height);
                        // doc.save('Test.pdf');
                        inputDict.footer = doc.output('blob');
                        document.querySelector('#campaignForm3').style.display = "block";
                        document.querySelector('#campaignForm4').style.display = "none";
                        document.querySelector('#campaignForm2').style.display = "none";
                        footerFile.value = "";
                        document.querySelector('#footerFileSpan').innerHTML = "Upload File";
                        info1.value = "";
                        info2.value = "";
                        tagline.value = "";
                        extraImage.value = "";
                        document.querySelector('#extraImageSpan').innerHTML = "Upload Image";
                    }
                });
            }else if(size == 3 && logoFile.files.length == 1 && brandName.value != "" && info1.value != ""){
                html2canvas(document.querySelector('#footerContainer'+size),{
                    onrendered: function(canvas){
                        let imgFooter = canvas.toDataURL('image/png');
                        let doc = new jsPDF('P','mm','a4');
                        let width = 84;
                        let height = 10;
                        doc.addImage(imgFooter,'PNG',3,3,width,height);
                        // doc.save('Test.pdf');
                        inputDict.footer = doc.output('blob');
                        document.querySelector('#campaignForm3').style.display = "block";
                        document.querySelector('#campaignForm4').style.display = "none";
                        document.querySelector('#campaignForm2').style.display = "none";
                        footerFile.value = "";
                        document.querySelector('#footerFileSpan').innerHTML = "Upload File";
                        info2.value = "";
                        tagline.value = "";
                        extraImage.value = "";
                        document.querySelector('#extraImageSpan').innerHTML = "Upload Image";
                    }
                });
            }else if(size == 4 && logoFile.files.length == 1 && brandName.value != "" && info1.value != "" && info2.value != ""){
                html2canvas(document.querySelector('#footerContainer'+size),{
                    onrendered: function(canvas){
                        let imgFooter = canvas.toDataURL('image/png');
                        let doc = new jsPDF('P','mm','a4');
                        let width = 120;
                        let height = 10;
                        doc.addImage(imgFooter,'PNG',3,3,width,height);
                        // doc.save('Test.pdf');
                        inputDict.footer = doc.output('blob');
                        document.querySelector('#campaignForm3').style.display = "block";
                        document.querySelector('#campaignForm4').style.display = "none";
                        document.querySelector('#campaignForm2').style.display = "none";
                        footerFile.value = "";
                        document.querySelector('#footerFileSpan').innerHTML = "Upload File";
                        tagline.value = "";
                        extraImage.value = "";
                        document.querySelector('#extraImageSpan').innerHTML = "Upload Image";
                    }
                });
            }else if(size == 5 && logoFile.files.length == 1 && brandName.value != "" && tagline.value != "" && info1.value != "" && info2.value != ""){
                html2canvas(document.querySelector('#footerContainer'+size),{
                    onrendered: function(canvas){
                        let imgFooter = canvas.toDataURL('image/png');
                        let doc = new jsPDF('P','mm','a4');
                        let width = 148;
                        let height = 10;
                        doc.addImage(imgFooter,'PNG',3,3,width,height);
                        // doc.save('Test.pdf');
                        inputDict.footer = doc.output('blob');
                        document.querySelector('#campaignForm3').style.display = "block";
                        document.querySelector('#campaignForm4').style.display = "none";
                        document.querySelector('#campaignForm2').style.display = "none";
                        footerFile.value = "";
                        document.querySelector('#footerFileSpan').innerHTML = "Upload File";
                        extraImage.value = "";
                        document.querySelector('#extraImageSpan').innerHTML = "Upload Image";
                    }
                });
            }else if(size == 6 || size == 7 && logoFile.files.length == 1 && brandName.value != "" && tagline.value != "" && info1.value != "" && info2.value != "" && extraImage.files.length == 1){
                html2canvas(document.querySelector('#footerContainer'+size),{
                    onrendered: function(canvas){
                        let imgFooter = canvas.toDataURL('image/png');
                        let doc = new jsPDF('P','mm','a4');
                        let width;
                        if(size == 6){
                            width = 176;
                        }else{
                            width = 200.377;
                        }
                        let height = 10;
                        doc.addImage(imgFooter,'PNG',3,3,width,height);
                        // doc.save('Test.pdf');
                        inputDict.footer = doc.output('blob');
                        document.querySelector('#campaignForm3').style.display = "block";
                        document.querySelector('#campaignForm4').style.display = "none";
                        document.querySelector('#campaignForm2').style.display = "none";
                        footerFile.value = "";
                        document.querySelector('#footerFileSpan').innerHTML = "Upload File";
                    }
                });
            }
            else{
                if(size >= 1 && logoFile.files.length != 1){
                    document.querySelector("#lblLogoFile").classList.add('is-invalid');
                }
                if(size >= 2 && brandName.value == ""){
                    brandName.classList.add('is-invalid');
                }
                if(size >= 3 && info1.value == ""){
                    info1.classList.add('is-invalid');
                }
                if(size >= 4 && info2.value == ""){
                    info2.classList.add('is-invalid');
                }
                if(size >= 5 && tagline.value == ""){
                    tagline.classList.add('is-invalid');
                }
                if(size >= 6 && extraImage.files.length != 1){
                    document.querySelector("#lblExtraImage").classList.add('is-invalid');
                }
            }
        }
        else{
            if(footerSize.value == ""){
                footerSize.classList.add("is-invalid");
            }
            if(footerType1.checked != true && footerType2.checked != true){
                document.querySelector('#footerType').classList.add("is-invalid");
            }
            if(footerType1.checked == true && footerFile.files.length != 1){
                document.querySelector("#lblFooterFile").classList.add('is-invalid');
            }
        }
    }
    function goToStep3p(){
        document.querySelector('#campaignForm3').style.display = "block";
        document.querySelector('#campaignForm4').style.display = "none";
        document.querySelector('#campaignForm2').style.display = "none";
    }
    function goToStep4(){
        let quantity = document.querySelector('#quantity').value;
        if(quantity != ""){
            showDict();
            document.querySelector('#spanCampaignName').innerHTML = inputDict.campaignName;
            document.querySelector('#spanCity').innerHTML = inputDict.city;
            document.querySelector('#spanLocality').innerHTML = inputDict.locality;
            document.querySelector('#spanSubLocality').innerHTML = inputDict.subLocality;
            document.querySelector('#spanCategory').innerHTML = inputDict.category;
            document.querySelector('#spanSubCategory').innerHTML = inputDict.subCategory;
            document.querySelector('#spanFooterSize').innerHTML = inputDict.footerSize;
            document.querySelector('#spanQuantity').innerHTML = inputDict.quantity;
            document.querySelector('#spanPrice').innerHTML = inputDict.price;
            document.querySelector('#campaignForm4').style.display = "block";
            document.querySelector('#campaignForm3').style.display = "none";
            document.querySelector('#campaignForm5').style.display = "none";
        }else{
            document.querySelector('#quantity').classList.add("is-invalid");
        }

    }
    function goToStep5(){
        document.querySelector('#campaignForm5').style.display = "block";
        document.querySelector('#campaignForm4').style.display = "none";
    }
    function payNow(){
        $.ajax({
            url:pathname,
            type:'post',
            contentType: 'application/json; charset=utf-8',
            data: inputDict,
            dataType: 'json',
            success: function(response){
                window.location.href = "/campaignSuccess.html"
            }
        })
    }

    // Profile js
    let profile = {
        "email":"abc22xyz@gmail.com",
        "firstName":"Abc",
        "lastName":"Xyz",
        "phoneNo":"9091929394",
        "city":"Pune",
        "zipcode":"411048"
    };
   //Campaign
   function showCampaignDetail(){
    console.log("hello");
   }