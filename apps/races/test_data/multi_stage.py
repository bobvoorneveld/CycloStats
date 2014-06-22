# -*- coding: utf-8 -*-
event_multi_stage_response = '''
<html>
<head>
<title>Sports Result Main</title>
<script type="text/javascript" language="JavaScript">
	<!--
	function Submit2SamePage(oForm) {
		oForm.elements[0].value = 19004;
		oForm.action = 'TheASP.asp';
		oForm.submit();
	};
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakeSeason() { this.length=1; return this; }
	SeasonID = new MakeSeason(); Season = new MakeSeason();
	SeasonID[0]=486; Season[0]="2014";
	// -->
</script>
<script type="text/javascript">

var gpxhr = null;
var gpxhr2 = null;
var gpxhr3 = null;

function processReqChange()
{
	var Vpv = document.getElementById('pri')

	if (gpxhr.readyState == 4)	{
	// 4 = "loaded"
	  if (gpxhr.status == 200)	{
		// 200 = "OK"
		Vpv.innerHTML = gpxhr.responseText;
		}
	  }
}

function processReqChange2()
{
	var Vpv = document.getElementById('seasoncombo')

	if (gpxhr2.readyState == 4)	{
	// 4 = "loaded"
	  if (gpxhr2.status == 200)	{
		// 200 = "OK"
		Vpv.innerHTML = gpxhr2.responseText;
		}
	  }
}

function Dropdown(sportid,competitionid,eventid,genderid,classid,seasonid,eventphaseid,phase1id,containereventid,detail,taalcode,styleid,cache)
{

	if (window.XMLHttpRequest) {
	  gpxhr = new XMLHttpRequest();
	}
	else if (window.ActiveXObject) {
	  gpxhr = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr!=null) {
		gpxhr.onreadystatechange = processReqChange;
		gpxhr.open('post','/asp/redirect/uci.asp?page=dropdown_ranking_phases&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&competitionid='+competitionid+'&eventid='+eventid+'&genderid='+genderid+'&classid='+classid+'&seasonid='+seasonid+'&eventphaseid='+eventphaseid+'&phase1id='+phase1id+'&containereventid='+containereventid+'&detail='+detail+'&cache='+cache);
		gpxhr.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

function fSeasonDropdown(sportid,competitionid,genderid,classid,ranking,detail,taalcode,styleid,cache)
{
	if (window.XMLHttpRequest) {
	  gpxhr2 = new XMLHttpRequest();
	}
	else if (window.ActiveXObject) {
	  gpxhr2 = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr2!=null) {
		gpxhr2.onreadystatechange = processReqChange2;
		if (competitionid == 26328){
			gpxhr2.open('post','/asp/redirect/uci.asp?page=dropdown_season&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+ '&competitionid='+ competitionid +'&genderid='+genderid+'&classid='+classid+'&ranking='+ranking+'&detail='+detail+'&cache='+cache);
		}else{
			gpxhr2.open('post','/asp/redirect/uci.asp?page=dropdown_season&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&genderid='+genderid+'&classid='+classid+'&ranking='+ranking+'&detail='+detail+'&cache='+cache);
		}
		gpxhr2.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

function fSeasonResultDropdown(sportid,competitionid,derivedcompetitionid,phasestatuscode,genderid,classid,ranking,detail,taalcode,styleid,cache)
{


	if (window.XMLHttpRequest) {
	  gpxhr2 = new XMLHttpRequest();
	}
	else if (window.ActiveXObject) {
	  gpxhr2 = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr2!=null) {
		gpxhr2.onreadystatechange = processReqChange2;
		gpxhr2.open('post','/asp/redirect/uci.asp?page=dropdown_season&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+ '&derivedcompetitionid='+derivedcompetitionid+'&phasestatuscode='+phasestatuscode+'&genderid='+genderid+'&classid='+classid+'&ranking='+ranking+'&detail='+detail+'&cache='+cache);
		gpxhr2.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

function processReqChange3()
{
	var Vpv = document.getElementById('personinfo')

	if (gpxhr3.readyState == 4)	{
	// 4 = "loaded"
	  if (gpxhr3.status == 200)	{
		// 200 = "OK"
		Vpv.innerHTML = gpxhr3.responseText;
		}
	  }
}

function PersonRankingInfo(sportid,seasonid,classid,genderid,derivedeventphaseid,derivedcompetitionid,derivedeventid,phase1id,personid,detail,taalcode,styleid,cache)
{
	if (window.XMLHttpRequest) {
	  gpxhr3 = new XMLHttpRequest();

	}
	else if (window.ActiveXObject) {
	  gpxhr3 = new ActiveXObject("Msxml2.XMLHTTP");
	}

	if (gpxhr3!=null) {
		gpxhr3.onreadystatechange = processReqChange3;
		gpxhr3.open("get",'/asp/redirect/uci.asp?page=personrankinginfo&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&seasonid='+seasonid+'&classid='+classid+'&genderid='+genderid+'&derivedeventphaseid='+derivedeventphaseid+'&derivedcompetitionid='+derivedcompetitionid+'&derivedeventid='+derivedeventid+'&phase1id='+phase1id+'&personid='+personid+'&detail='+detail+'&cache='+cache);
		//document.write('/asp/redirect/uci.asp?page=personrankinginfo&TaalCode='+taalcode+'&StyleID='+styleid+'&sportid='+sportid+'&seasonid='+seasonid+'&classid='+classid+'&genderid='+genderid+'&derivedeventphaseid='+derivedeventphaseid+'&derivedcompetitionid='+derivedcompetitionid+'&derivedeventid='+derivedeventid+'&phase1id='+phase1id+'&personid='+personid+'&detail='+detail+'&cache='+cache);
        //gpxhr3.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        //gpxhr3.setRequestHeader("Content-Type", "text/xml; charset=iso-8859-9");
	    //gpxhr3.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
		gpxhr3.send('');
	}
	else {
		alert("Your browser does not support XMLHTTP.");
	}
}

</script>

<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<link rel="StyleSheet" href="/css/uci.css" type="text/css">
<script type="text/javascript">
<!--

document.domain='infostradasports.com';

//-->
</script>
<SCRIPT LANGUAGE="JavaScript">
<!--

function scroll2top()
{
	this.window.scrollTo(0,0);
	parent.window.scrollTo(0,0);
}

function loadnav()
{
	slocation = '/asp/navigation_competitions.asp'+window.location.search;
	if (parent.frames['vmenul']) {
		parent.frames['vmenul'].document.location=slocation;
	}
}
// -->
</SCRIPT>
</head>

<body onload="scroll2top();loadnav();document.getElementById('loader').style.display= 'none'">
<img src="/images/icons/loader.gif" id="loader" style="position:absolute; left:50%; top:50%;">


<table  cellspacing="0" cellpadding="0" border=0 width="100%">
<tr><td width="22"><img src="/images/nix.gif" width="22" height="1"></td><td>
<table  cellspacing="0" cellpadding="0" border="0" width="100%"><tr><td valign="top">
<div class="crumblepad">
	<span class="crumblepad_header">Results - Cycling - Road 2014</span>
	<br/><br/>
	Men
	<img src="/images/icons/bullet.gif">
	Elite
	<img src="/images/icons/bullet.gif">
	Tour de Suisse
	(SUI/UWT)
</div>
<img src="/images/nix.gif" width=1 height=22 border=0>

</td><td valign="top" width=120>
<div id="seasoncombo" style="float:right;display:inline;padding-top:5px;">
<script type="text/javascript">
fSeasonResultDropdown(102, 20583, -1, 262280, 1, 1, 0, 1, 2, 0, 8)
</script>
</div>
</td></tr></table>

<table width="100%" border="0" cellspacing="0" cellpadding="3" class="datatable">
<tr>
	<td class="caption">Date</td>
	<td class="caption">Race</td>
	<td class="caption">Winner</td>
	<td class="caption">Leader</td>
</tr>
<tr valign="top">
	<td><nobr>14&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">General classification</a></td>
	<td>FARIA DA COSTA (POR)</td>
	<td>&nbsp;</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898892&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 9</a></td>
	<td>FARIA DA COSTA (POR)</td>
	<td>FARIA DA COSTA (POR)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898891&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 8</a></td>
	<td>CHAVES RUBIO  (COL)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898890&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 7 (ITT)</a></td>
	<td>MARTIN (GER)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898889&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 6</a></td>
	<td>TRENTIN (ITA)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898888&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 5</a></td>
	<td>MODOLO (ITA)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898887&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 4</a></td>
	<td>CAVENDISH (GBR)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898886&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 3</a></td>
	<td>SAGAN (SVK)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898885&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 2</a></td>
	<td>MEYER (AUS)</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>14&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&GenderID=1&ClassID=1&Phase1ID=898884&Phase2ID=0&Phase3ID=0&DerivedEventPhaseID=-1&Detail=1&Ranking=0">Stage 1 (ITT)</a></td>
	<td>MARTIN (GER)</td>
	<td>MARTIN (GER)</td>
</tr>
</table>
<table width="98%" border="0" cellspacing="0" cellpadding="2" class="datatablelegend">
</table>
</td><td width="5"><img src="/images/nix.gif" width="5" height="1"></td></tr></table>
<br /><img src="/images/libs/nix.gif" width=1  height=5 border=0>

</font>
</body>
</html>
'''
