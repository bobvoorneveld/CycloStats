# -*- coding: utf-8 -*-
event_response = '''
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
	function MakeSeason() { this.length=6; return this; }
	SeasonID = new MakeSeason(); Season = new MakeSeason();
	SeasonID[0]=486; Season[0]="2014";
	SeasonID[1]=484; Season[1]="2013";
	SeasonID[2]=482; Season[2]="2012";
	SeasonID[3]=480; Season[3]="2011";
	SeasonID[4]=478; Season[4]="2010";
	SeasonID[5]=476; Season[5]="2009";
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
<div class="downloadpdf" align = "right">
		<a href="/asp/redirect/uci.asp?page=nationalchampions&SportID=102" target="_blank">National Champions</a>
</div>

<table  cellspacing="0" cellpadding="0" border="0" width="100%"><tr><td valign="top">
<div class="crumblepad">
	<span class="crumblepad_header">Results - Cycling - Road 2014</span>
	<br/> <br/>
	Men
	<img src="/images/icons/bullet.gif">
	Elite
</div>
<img src="/images/nix.gif" width=1 height=22 border=0 alt="">

</td><td valign="top" width=120>
<div id="seasoncombo" style="float:right;display:inline;padding-top:5px;">
<script type="text/javascript">
fSeasonResultDropdown(102, -1, -1, 262280, 1, 1, 0, 1, 2, 0, 8)
</script>
</div>
</td></tr></table>

<table width="100%" border="0" cellspacing="0" cellpadding="3" class="datatable">
<tr>
	<td class="caption">Date</td>
	<td class="caption">Event</td>
	<td class="caption">Nat.</td>
	<td class="caption">Class</td>
	<td class="caption">Winner</td>
</tr>
<tr valign="top">
	<td><nobr>14&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventID=12146&EventPhaseID=888147&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Suisse <i>(in&nbsp;progress)</i></a></td>
	<td>SUI</td>
	<td>UWT</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21629&CompetitionCodeInv=1&EditionID=891461&SeasonID=486&EventID=12146&EventPhaseID=891877&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Iran (Azerbaijan) <i>(in&nbsp;progress)</i></a></td>
	<td>IRI</td>
	<td>2.1</td>
	<td>MIZBANI IRANAGH (IRI)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21618&CompetitionCodeInv=1&EditionID=891457&SeasonID=486&EventID=12146&EventPhaseID=891873&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ster ZLM Toer GP Jan van Heeswijk <i>(in&nbsp;progress)</i></a></td>
	<td>NED</td>
	<td>2.1</td>
	<td>KITTEL (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20543&CompetitionCodeInv=1&EditionID=891370&SeasonID=486&EventID=12146&EventPhaseID=891789&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Slovénie <i>(in&nbsp;progress)</i></a></td>
	<td>SLO</td>
	<td>2.1</td>
	<td>MATTHEWS (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=24042&CompetitionCodeInv=1&EditionID=891622&SeasonID=486&EventID=12146&EventPhaseID=892009&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour des Pays de Savoie <i>(in&nbsp;progress)</i></a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>IGNATYEV (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=24628&CompetitionCodeInv=1&EditionID=891635&SeasonID=486&EventID=12146&EventPhaseID=892021&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Oberösterreichrundfahrt <i>(in&nbsp;progress)</i></a></td>
	<td>AUT</td>
	<td>2.2</td>
	<td>VAN DER HAAR (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Jun-22&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20587&CompetitionCodeInv=1&EditionID=891383&SeasonID=486&EventID=12146&EventPhaseID=891803&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Route du Sud - la Dépêche du Midi <i>(in&nbsp;progress)</i></a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>HERRADA LOPEZ (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Jun-21&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20594&CompetitionCodeInv=1&EditionID=891385&SeasonID=486&EventID=12146&EventPhaseID=891805&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Serbie <i>(in&nbsp;progress)</i></a></td>
	<td>SRB</td>
	<td>2.2</td>
	<td>KOWALCZYK (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>07&nbsp;Jun-15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=24057&CompetitionCodeInv=1&EditionID=891625&SeasonID=486&EventID=12146&EventPhaseID=892012&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Singkarak</a></td>
	<td>INA</td>
	<td>2.2</td>
	<td>ZARGARI (IRI)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Jun-15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22207&CompetitionCodeInv=1&EditionID=891489&SeasonID=486&EventID=12146&EventPhaseID=891906&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Korea</a></td>
	<td>KOR</td>
	<td>2.1</td>
	<td>CARTHY (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Jun-15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20571&CompetitionCodeInv=1&EditionID=888109&SeasonID=486&EventID=12146&EventPhaseID=888146&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Critérium du Dauphiné</a></td>
	<td>FRA</td>
	<td>UWT</td>
	<td>TALANSKY (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;Jun-15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20590&CompetitionCodeInv=1&EditionID=891384&SeasonID=486&EventID=12146&EventPhaseID=891804&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Beauce</a></td>
	<td>CAN</td>
	<td>2.2</td>
	<td>SKUJINS (LAT)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;Jun-15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26605&CompetitionCodeInv=1&EditionID=891723&SeasonID=486&EventID=12146&EventPhaseID=892099&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix "Udmurtskaya Pravda"</a></td>
	<td>RUS</td>
	<td>2.2</td>
	<td>ERSHOV (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Jun-15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23733&CompetitionCodeInv=1&EditionID=891592&SeasonID=486&EventID=12146&EventPhaseID=891983&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ronde de l'Oise</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>NIELSEN (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22527&CompetitionCodeInv=1&EditionID=891420&SeasonID=486&EventID=10635&EventPhaseID=891839&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ronde van Limburg</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>VAN DER POEL (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21570&CompetitionCodeInv=1&EditionID=891453&SeasonID=486&EventID=10635&EventPhaseID=891869&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Int. Raiffeisen Grand Prix</a></td>
	<td>AUT</td>
	<td>1.2</td>
	<td>ROGINA (CRO)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23985&CompetitionCodeInv=1&EditionID=938938&SeasonID=486&EventID=10636&EventPhaseID=938942&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National du Liban ITT</a></td>
	<td>LIB</td>
	<td>CN</td>
	<td>ABOU (LIB)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22678&CompetitionCodeInv=1&EditionID=958714&SeasonID=486&EventID=10636&EventPhaseID=958734&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National de Costa Rica ITT</a></td>
	<td>CRC</td>
	<td>CN</td>
	<td>GONZÁLEZ (CRC)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Jun-14&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23337&CompetitionCodeInv=1&EditionID=891574&SeasonID=486&EventID=12146&EventPhaseID=891966&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Malopolska</a></td>
	<td>POL</td>
	<td>2.2</td>
	<td>WERDA (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20538&CompetitionCodeInv=1&EditionID=888184&SeasonID=486&EventID=10635&EventPhaseID=888237&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">GP du canton d'Argovie</a></td>
	<td>SUI</td>
	<td>1.HC</td>
	<td>GESCHKE (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;Jun-08&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20576&CompetitionCodeInv=1&EditionID=888188&SeasonID=486&EventID=12146&EventPhaseID=888241&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Skoda-Tour de Luxembourg</a></td>
	<td>LUX</td>
	<td>2.HC</td>
	<td>BRESCHEL (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Jun-08&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23297&CompetitionCodeInv=1&EditionID=891563&SeasonID=486&EventID=12146&EventPhaseID=891958&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Boucles de la Mayenne</a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>ROSSETTO (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Jun-08&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23923&CompetitionCodeInv=1&EditionID=891608&SeasonID=486&EventID=12146&EventPhaseID=892210&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix Cycliste de Saguenay</a></td>
	<td>CAN</td>
	<td>2.2</td>
	<td>KOCJAN (SLO)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22516&CompetitionCodeInv=1&EditionID=891511&SeasonID=486&EventID=10635&EventPhaseID=891923&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Coppa della Pace - Trofeo F.lli Anelli</a></td>
	<td>ITA</td>
	<td>1.2</td>
	<td>CEOLAN (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21577&CompetitionCodeInv=1&EditionID=891455&SeasonID=486&EventID=10635&EventPhaseID=891871&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Memorial Philippe Van Coningsloo</a></td>
	<td>BEL</td>
	<td>1.2</td>
	<td>RUIJGH (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>03&nbsp;Jun-07&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22151&CompetitionCodeInv=1&EditionID=891486&SeasonID=486&EventID=12146&EventPhaseID=891903&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Slovaquie</a></td>
	<td>SVK</td>
	<td>2.2</td>
	<td>POLIVODA (UKR)</td>
</tr>
<tr valign="top">
	<td><nobr>07&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25842&CompetitionCodeInv=1&EditionID=891688&SeasonID=486&EventID=10635&EventPhaseID=892070&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ronde Van Zeeland Seaports</a></td>
	<td>NED</td>
	<td>1.1</td>
	<td>BOS (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21464&CompetitionCodeInv=1&EditionID=952926&SeasonID=486&EventID=10636&EventPhaseID=952930&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National de Slovenie ITT</a></td>
	<td>SLO</td>
	<td>CN</td>
	<td>GAZVODA (SLO)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20561&CompetitionCodeInv=1&EditionID=891379&SeasonID=486&EventID=10635&EventPhaseID=891798&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Alcide Degasperi</a></td>
	<td>ITA</td>
	<td>1.2</td>
	<td>GAZZARRA (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20559&CompetitionCodeInv=1&EditionID=888108&SeasonID=486&EventID=12146&EventPhaseID=888145&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Giro d'Italia</a></td>
	<td>ITA</td>
	<td>UWT</td>
	<td>QUINTANA ROJAS (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20566&CompetitionCodeInv=1&EditionID=888187&SeasonID=486&EventID=12146&EventPhaseID=888240&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Bayern Rundfahrt</a></td>
	<td>GER</td>
	<td>2.HC</td>
	<td>THOMAS (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21413&CompetitionCodeInv=1&EditionID=888205&SeasonID=486&EventID=12146&EventPhaseID=888259&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Baloise Belgium Tour</a></td>
	<td>BEL</td>
	<td>2.HC</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22040&CompetitionCodeInv=1&EditionID=891478&SeasonID=486&EventID=12146&EventPhaseID=891893&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Flèche du Sud</a></td>
	<td>LUX</td>
	<td>2.2</td>
	<td>BILLE (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23961&CompetitionCodeInv=1&EditionID=891613&SeasonID=486&EventID=12146&EventPhaseID=892000&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour des Fjords</a></td>
	<td>NOR</td>
	<td>2.1</td>
	<td>KRISTOFF (NOR)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23905&CompetitionCodeInv=1&EditionID=891604&SeasonID=486&EventID=12146&EventPhaseID=891994&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Kumano</a></td>
	<td>JPN</td>
	<td>2.2</td>
	<td>MANCEBO PEREZ (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22047&CompetitionCodeInv=1&EditionID=891480&SeasonID=486&EventID=12146&EventPhaseID=891894&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Gironde</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>TE BRAKE (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22054&CompetitionCodeInv=1&EditionID=891481&SeasonID=486&EventID=10635&EventPhaseID=891895&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Asian Cycling Championships RR</a></td>
	<td>KAZ</td>
	<td>CC</td>
	<td>TLEUBAYEV (KAZ)</td>
</tr>
<tr valign="top">
	<td><nobr>31&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25441&CompetitionCodeInv=1&EditionID=952757&SeasonID=486&EventID=10635&EventPhaseID=952765&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - ERI RR</a></td>
	<td>ERI</td>
	<td>CN</td>
	<td>GEBREZGABIHIER (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25645&CompetitionCodeInv=1&EditionID=891680&SeasonID=486&EventID=10635&EventPhaseID=892062&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix Südkärnten</a></td>
	<td>AUT</td>
	<td>1.2</td>
	<td>PASQUALON (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26610&CompetitionCodeInv=1&EditionID=891728&SeasonID=486&EventID=10635&EventPhaseID=892104&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Race Horizon Park 3</a></td>
	<td>UKR</td>
	<td>1.2</td>
	<td>KOSTYUK (UKR)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20581&CompetitionCodeInv=1&EditionID=891382&SeasonID=486&EventID=10635&EventPhaseID=891801&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">The Philadelphia Cycling Classic</a></td>
	<td>USA</td>
	<td>1.1</td>
	<td>REIJNEN (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20847&CompetitionCodeInv=1&EditionID=891433&SeasonID=486&EventID=10635&EventPhaseID=891851&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Boucles de l'Aulne - Châteaulin</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>GOUGEARD (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>30&nbsp;May-31&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23047&CompetitionCodeInv=1&EditionID=891551&SeasonID=486&EventID=12146&EventPhaseID=891948&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Estonia</a></td>
	<td>EST</td>
	<td>2.1</td>
	<td>GROSU (ROU)</td>
</tr>
<tr valign="top">
	<td><nobr>31&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26140&CompetitionCodeInv=1&EditionID=891713&SeasonID=486&EventID=10635&EventPhaseID=892090&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Race Horizon Park 2</a></td>
	<td>UKR</td>
	<td>1.2</td>
	<td>KONONENKO (UKR)</td>
</tr>
<tr valign="top">
	<td><nobr>31&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20511&CompetitionCodeInv=1&EditionID=891359&SeasonID=486&EventID=10635&EventPhaseID=891780&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix de Plumelec-Morbihan</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>SIMON (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>31&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25441&CompetitionCodeInv=1&EditionID=952757&SeasonID=486&EventID=10636&EventPhaseID=952762&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - ERI ITT</a></td>
	<td>ERI</td>
	<td>CN</td>
	<td>BERHANE (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>30&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25644&CompetitionCodeInv=1&EditionID=891679&SeasonID=486&EventID=10635&EventPhaseID=892061&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Race Horizon Park 1</a></td>
	<td>UKR</td>
	<td>1.2</td>
	<td>BUTS (UKR)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;May-01&nbsp;Jun&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22054&CompetitionCodeInv=1&EditionID=891481&SeasonID=486&EventID=10636&EventPhaseID=891897&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Asian Cycling Championships ITT</a></td>
	<td>KAZ</td>
	<td>CC</td>
	<td>GRUZDEV (KAZ)</td>
</tr>
<tr valign="top">
	<td><nobr>24&nbsp;May-26&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20749&CompetitionCodeInv=1&EditionID=938908&SeasonID=486&EventID=10635&EventPhaseID=938913&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - USA RR</a></td>
	<td>USA</td>
	<td>CN</td>
	<td>MARCOTTE (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;May-25&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22578&CompetitionCodeInv=1&EditionID=891515&SeasonID=486&EventID=12146&EventPhaseID=891926&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">An Post Ras</a></td>
	<td>IRL</td>
	<td>2.2</td>
	<td>FANKHAUSER (AUT)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;May-25&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20558&CompetitionCodeInv=1&EditionID=891378&SeasonID=486&EventID=12146&EventPhaseID=891797&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Japan</a></td>
	<td>JPN</td>
	<td>2.1</td>
	<td>POURSEYEDIGOLAKHOUR (IRI)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;May-25&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26182&CompetitionCodeInv=1&EditionID=888225&SeasonID=486&EventID=12146&EventPhaseID=888279&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Norway</a></td>
	<td>NOR</td>
	<td>2.HC</td>
	<td>PATERSKI (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>23&nbsp;May-25&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26115&CompetitionCodeInv=1&EditionID=891708&SeasonID=486&EventID=12146&EventPhaseID=892086&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris-Arras Tour</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>VANTOMME (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>24&nbsp;May-25&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=25647&CompetitionCodeInv=1&EditionID=891682&SeasonID=486&EventID=12146&EventPhaseID=892064&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">World Ports Classic</a></td>
	<td>NED</td>
	<td>2.1</td>
	<td>BOS (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>25&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21532&CompetitionCodeInv=1&EditionID=891449&SeasonID=486&EventID=10635&EventPhaseID=891865&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Simac Omloop der Kempen</a></td>
	<td>NED</td>
	<td>1.2</td>
	<td>DAVISON (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>24&nbsp;May-26&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20749&CompetitionCodeInv=1&EditionID=938908&SeasonID=486&EventID=10636&EventPhaseID=938911&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - USA ITT</a></td>
	<td>USA</td>
	<td>CN</td>
	<td>PHINNEY (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;May-18&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23603&CompetitionCodeInv=1&EditionID=888212&SeasonID=486&EventID=12146&EventPhaseID=888266&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Amgen Tour of California</a></td>
	<td>USA</td>
	<td>2.HC</td>
	<td>WIGGINS (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;May-18&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22562&CompetitionCodeInv=1&EditionID=891514&SeasonID=486&EventID=12146&EventPhaseID=891925&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Rhône-Alpes Isère Tour</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>KVASINA (CRO)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;May-18&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20556&CompetitionCodeInv=1&EditionID=891377&SeasonID=486&EventID=12146&EventPhaseID=891796&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Picardie</a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>DEMARE (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;May-18&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20645&CompetitionCodeInv=1&EditionID=891392&SeasonID=486&EventID=12146&EventPhaseID=891812&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta a Castilla y Leon</a></td>
	<td>ESP</td>
	<td>2.1</td>
	<td>BELDA GARCIA (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25160&CompetitionCodeInv=1&EditionID=891647&SeasonID=486&EventID=10635&EventPhaseID=892029&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Garmin Velothon Berlin</a></td>
	<td>GER</td>
	<td>1.1</td>
	<td>KREDER (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;May-17&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20555&CompetitionCodeInv=1&EditionID=891376&SeasonID=486&EventID=12146&EventPhaseID=891795&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Royal Smilde Olympia's Tour</a></td>
	<td>NED</td>
	<td>2.2</td>
	<td>DE VRIES (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26809&CompetitionCodeInv=1&EditionID=920924&SeasonID=486&EventID=10635&EventPhaseID=920925&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Visegrad 4 Bicycle Race - GP Hungary</a></td>
	<td>HUN</td>
	<td>1.2</td>
	<td>BERNAS (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21671&CompetitionCodeInv=1&EditionID=891469&SeasonID=486&EventID=10635&EventPhaseID=891885&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix Criquielion</a></td>
	<td>BEL</td>
	<td>1.2</td>
	<td>PEETERS (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26772&CompetitionCodeInv=1&EditionID=906830&SeasonID=486&EventID=10635&EventPhaseID=906832&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Visegrad 4 Bicycle Race - GP Slovakia</a></td>
	<td>SVK</td>
	<td>1.2</td>
	<td>BERNAS (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26810&CompetitionCodeInv=1&EditionID=920922&SeasonID=486&EventID=10635&EventPhaseID=920923&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Visegrad 4 Bicycle Race - GP Czech Republic</a></td>
	<td>CZE</td>
	<td>1.2</td>
	<td>CERNY (CZE)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26817&CompetitionCodeInv=1&EditionID=922798&SeasonID=486&EventID=10635&EventPhaseID=922799&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Visegrad 4 Bicycle Race - GP Polski Via Odra</a></td>
	<td>POL</td>
	<td>1.2</td>
	<td>BASKA (SVK)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=24608&CompetitionCodeInv=1&EditionID=891630&SeasonID=486&EventID=10635&EventPhaseID=892017&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Challenge du Prince - Trophée de la Maison Royale</a></td>
	<td>MAR</td>
	<td>1.2</td>
	<td>CHAOUFI (MAR)</td>
</tr>
<tr valign="top">
	<td><nobr>07&nbsp;May-11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=25640&CompetitionCodeInv=1&EditionID=891678&SeasonID=486&EventID=12146&EventPhaseID=892060&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour d'Azerbaïdjan</a></td>
	<td>AZE</td>
	<td>2.1</td>
	<td>ZAKARIN (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>07&nbsp;May-11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20544&CompetitionCodeInv=1&EditionID=888185&SeasonID=486&EventID=12146&EventPhaseID=888238&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">4 Jours de Dunkerque / Tour du Nord-pas-de-Calais</a></td>
	<td>FRA</td>
	<td>2.HC</td>
	<td>DEMARE (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;May-11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21621&CompetitionCodeInv=1&EditionID=891459&SeasonID=486&EventID=12146&EventPhaseID=891875&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Szlakiem Grodòw Piastowskich</a></td>
	<td>POL</td>
	<td>2.1</td>
	<td>TACIAK (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21624&CompetitionCodeInv=1&EditionID=891460&SeasonID=486&EventID=10635&EventPhaseID=891876&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ringerike GP</a></td>
	<td>NOR</td>
	<td>1.2</td>
	<td>NIELSEN (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;May-11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22242&CompetitionCodeInv=1&EditionID=891493&SeasonID=486&EventID=10635&EventPhaseID=891909&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Champ. Panaméricain / Pan American Champ. RR</a></td>
	<td>MEX</td>
	<td>CC</td>
	<td>GUAMA DE LA CRUZ (ECU)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22515&CompetitionCodeInv=1&EditionID=891510&SeasonID=486&EventID=10635&EventPhaseID=891922&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Circuit de Wallonie Ville de Fleurus</a></td>
	<td>BEL</td>
	<td>1.2</td>
	<td>LAMMERTINK (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=24607&CompetitionCodeInv=1&EditionID=891629&SeasonID=486&EventID=10635&EventPhaseID=892016&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Challenge du Prince - Trophée de l'Anniversaire</a></td>
	<td>MAR</td>
	<td>1.2</td>
	<td>LAHSAINI (MAR)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23277&CompetitionCodeInv=1&EditionID=891562&SeasonID=486&EventID=10635&EventPhaseID=891957&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Scandinavian Race in Uppsala</a></td>
	<td>SWE</td>
	<td>1.2</td>
	<td>JÖRGENSEN (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26139&CompetitionCodeInv=1&EditionID=891712&SeasonID=486&EventID=10635&EventPhaseID=892089&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Hadeland GP</a></td>
	<td>NOR</td>
	<td>1.2</td>
	<td>GULDHAMMER (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21404&CompetitionCodeInv=1&EditionID=891444&SeasonID=486&EventID=10635&EventPhaseID=891860&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Berner-Rundfahrt / Tour de Berne</a></td>
	<td>SUI</td>
	<td>1.2</td>
	<td>BRANDLE (AUT)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;May-09&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22705&CompetitionCodeInv=1&EditionID=891524&SeasonID=486&EventID=12146&EventPhaseID=891933&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Five rings of Moscow</a></td>
	<td>RUS</td>
	<td>2.2</td>
	<td>SOLOMENNIKOV (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=24606&CompetitionCodeInv=1&EditionID=891628&SeasonID=486&EventID=10635&EventPhaseID=892015&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Challenge du Prince - Trophée Princier</a></td>
	<td>MAR</td>
	<td>1.2</td>
	<td>SAADOUNE (MAR)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;May-11&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22242&CompetitionCodeInv=1&EditionID=891493&SeasonID=486&EventID=10636&EventPhaseID=891911&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Champ. Panaméricain / Pan American Champ. ITT</a></td>
	<td>MEX</td>
	<td>CC</td>
	<td>HERRERA (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr-04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22697&CompetitionCodeInv=1&EditionID=888208&SeasonID=486&EventID=12146&EventPhaseID=888262&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Presidential Cycling Tour of Turkey</a></td>
	<td>TUR</td>
	<td>2.HC</td>
	<td>YATES (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;Apr-04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20542&CompetitionCodeInv=1&EditionID=888107&SeasonID=486&EventID=12146&EventPhaseID=888144&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Romandie</a></td>
	<td>SUI</td>
	<td>UWT</td>
	<td>FROOME (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>30&nbsp;Apr-04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21237&CompetitionCodeInv=1&EditionID=891440&SeasonID=486&EventID=12146&EventPhaseID=891857&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of the Gila</a></td>
	<td>USA</td>
	<td>2.2</td>
	<td>JONES (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20550&CompetitionCodeInv=1&EditionID=891372&SeasonID=486&EventID=10635&EventPhaseID=891791&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Circuito del Porto - Trofeo Arvedi</a></td>
	<td>ITA</td>
	<td>1.2</td>
	<td>MARECZKO (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22136&CompetitionCodeInv=1&EditionID=891484&SeasonID=486&EventID=10635&EventPhaseID=891901&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix de la Somme « Conseil Général 80»</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>HUTAROVICH (BLR)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26114&CompetitionCodeInv=1&EditionID=891707&SeasonID=486&EventID=10635&EventPhaseID=892085&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Destination Thy</a></td>
	<td>DEN</td>
	<td>1.2</td>
	<td>NIELSEN (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;May-04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22589&CompetitionCodeInv=1&EditionID=948173&SeasonID=486&EventID=10635&EventPhaseID=948180&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National d'Argentine RR</a></td>
	<td>ARG</td>
	<td>CN</td>
	<td>DIAZ (ARG)</td>
</tr>
<tr valign="top">
	<td><nobr>03&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25155&CompetitionCodeInv=1&EditionID=891643&SeasonID=486&EventID=10635&EventPhaseID=892027&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Himmerland Rundt</a></td>
	<td>DEN</td>
	<td>1.2</td>
	<td>NIELSEN (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>03&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23317&CompetitionCodeInv=1&EditionID=891567&SeasonID=486&EventID=10635&EventPhaseID=891962&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix of Moscow</a></td>
	<td>RUS</td>
	<td>1.2</td>
	<td>KRASNOV (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>03&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21530&CompetitionCodeInv=1&EditionID=891448&SeasonID=486&EventID=10635&EventPhaseID=891864&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">62ste Ronde van Overijssel</a></td>
	<td>NED</td>
	<td>1.2</td>
	<td>COENEN (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23318&CompetitionCodeInv=1&EditionID=891568&SeasonID=486&EventID=10635&EventPhaseID=891963&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Memorial of Oleg Dyachenko</a></td>
	<td>RUS</td>
	<td>1.2</td>
	<td>SOLOMENNIKOV (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26112&CompetitionCodeInv=1&EditionID=891706&SeasonID=486&EventID=10635&EventPhaseID=892084&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Skive-Løbet</a></td>
	<td>DEN</td>
	<td>1.2</td>
	<td>BAUHAUS (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;May-04&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22589&CompetitionCodeInv=1&EditionID=948173&SeasonID=486&EventID=10636&EventPhaseID=948176&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National d'Argentine ITT</a></td>
	<td>ARG</td>
	<td>CN</td>
	<td>ROSAS (ARG)</td>
</tr>
<tr valign="top">
	<td><nobr>25&nbsp;Apr-01&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20529&CompetitionCodeInv=1&EditionID=892236&SeasonID=486&EventID=12146&EventPhaseID=891914&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Le Tour de Bretagne Cycliste trophée harmonie Mutuelle</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>LINDEMAN (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20531&CompetitionCodeInv=1&EditionID=888183&SeasonID=486&EventID=10635&EventPhaseID=888236&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Rund um den Finanzplatz Eschborn-Frankfurt</a></td>
	<td>GER</td>
	<td>1.HC</td>
	<td>KRISTOFF (NOR)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23316&CompetitionCodeInv=1&EditionID=891566&SeasonID=486&EventID=10635&EventPhaseID=891961&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Mayor Cup</a></td>
	<td>RUS</td>
	<td>1.2</td>
	<td>LAGUTIN (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23133&CompetitionCodeInv=1&EditionID=891553&SeasonID=486&EventID=10635&EventPhaseID=891949&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Memorial Andrzeja Trochanowskiego</a></td>
	<td>POL</td>
	<td>1.2</td>
	<td>GRADEK (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;May&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20595&CompetitionCodeInv=1&EditionID=920788&SeasonID=486&EventID=10636&EventPhaseID=920795&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National de Belgique ITT</a></td>
	<td>BEL</td>
	<td>CN</td>
	<td>VANDEWALLE (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>23&nbsp;Apr-27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23446&CompetitionCodeInv=1&EditionID=891578&SeasonID=486&EventID=12146&EventPhaseID=891970&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Volta do Paraná</a></td>
	<td>BRA</td>
	<td>2.2</td>
	<td>MANARELLI (BRA)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23906&CompetitionCodeInv=1&EditionID=891605&SeasonID=486&EventID=10635&EventPhaseID=891995&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Melaka Chief Minister's Cup</a></td>
	<td>MAS</td>
	<td>1.2</td>
	<td>PLIUSCHIN (MDA)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23159&CompetitionCodeInv=1&EditionID=891555&SeasonID=486&EventID=10635&EventPhaseID=891951&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">La Roue Tourangelle Région Centre - Classic Loire Touraine Vignobles & Chateaux</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>TULIK (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22424&CompetitionCodeInv=1&EditionID=891499&SeasonID=486&EventID=10635&EventPhaseID=891919&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Rutland - Melton International CiCLE Classic</a></td>
	<td>GBR</td>
	<td>1.2</td>
	<td>MOSES (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22711&CompetitionCodeInv=1&EditionID=891525&SeasonID=486&EventID=10635&EventPhaseID=891934&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Gran Premio Industrie del Marmo</a></td>
	<td>ITA</td>
	<td>1.2</td>
	<td>MUGERLI (SLO)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20513&CompetitionCodeInv=1&EditionID=888105&SeasonID=486&EventID=10635&EventPhaseID=888142&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Liège - Bastogne - Liège</a></td>
	<td>BEL</td>
	<td>UWT</td>
	<td>GERRANS (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20551&CompetitionCodeInv=1&EditionID=891373&SeasonID=486&EventID=10635&EventPhaseID=891792&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris - Mantes-en-Yvelines</a></td>
	<td>FRA</td>
	<td>1.2</td>
	<td>MENUT (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>26&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23647&CompetitionCodeInv=1&EditionID=891591&SeasonID=486&EventID=10635&EventPhaseID=891982&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Zuid Oost Drenthe Classic I</a></td>
	<td>NED</td>
	<td>1.2</td>
	<td>STROETINGA (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Apr-25&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20546&CompetitionCodeInv=1&EditionID=888186&SeasonID=486&EventID=12146&EventPhaseID=888239&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Giro del Trentino</a></td>
	<td>ITA</td>
	<td>2.HC</td>
	<td>EVANS (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Apr-24&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21619&CompetitionCodeInv=1&EditionID=891458&SeasonID=486&EventID=12146&EventPhaseID=891874&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Le Tour de Filipinas</a></td>
	<td>PHI</td>
	<td>2.2</td>
	<td>GALEDO (PHI)</td>
</tr>
<tr valign="top">
	<td><nobr>23&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20507&CompetitionCodeInv=1&EditionID=888104&SeasonID=486&EventID=10635&EventPhaseID=888141&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">La Flèche Wallonne</a></td>
	<td>BEL</td>
	<td>UWT</td>
	<td>VALVERDE BELMONTE (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20565&CompetitionCodeInv=1&EditionID=891381&SeasonID=486&EventID=10635&EventPhaseID=891800&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Rund um Köln</a></td>
	<td>GER</td>
	<td>1.1</td>
	<td>BENNETT (IRL)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Apr-20&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22693&CompetitionCodeInv=1&EditionID=891523&SeasonID=486&EventID=12146&EventPhaseID=891932&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour du Loir et Cher E Provost</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>BRIGGS (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Apr-20&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=25173&CompetitionCodeInv=1&EditionID=891654&SeasonID=486&EventID=12146&EventPhaseID=892036&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix of Adygeya</a></td>
	<td>RUS</td>
	<td>2.2</td>
	<td>ZAKARIN (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21635&CompetitionCodeInv=1&EditionID=891463&SeasonID=486&EventID=10635&EventPhaseID=891879&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tro-Bro Léon</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>PETIT (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20523&CompetitionCodeInv=1&EditionID=888106&SeasonID=486&EventID=10635&EventPhaseID=888143&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Amstel Gold Race</a></td>
	<td>NED</td>
	<td>UWT</td>
	<td>GILBERT (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22039&CompetitionCodeInv=1&EditionID=891477&SeasonID=486&EventID=10635&EventPhaseID=891892&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour du Finistère</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>DEMOITIE (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23979&CompetitionCodeInv=1&EditionID=891619&SeasonID=486&EventID=10635&EventPhaseID=892006&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Arno Wallaard Memorial</a></td>
	<td>NED</td>
	<td>1.2</td>
	<td>WILSSON (SWE)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26616&CompetitionCodeInv=1&EditionID=891733&SeasonID=486&EventID=10635&EventPhaseID=892109&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Winston Salem Cycling Classic</a></td>
	<td>USA</td>
	<td>1.2</td>
	<td>MCCABE (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20519&CompetitionCodeInv=1&EditionID=891363&SeasonID=486&EventID=10635&EventPhaseID=891783&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">GP de Denain Porte du Hainaut</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>BOUHANNI (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20486&CompetitionCodeInv=1&EditionID=888181&SeasonID=486&EventID=10635&EventPhaseID=888234&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">De Brabantse Pijl - La Flèche Brabançonne</a></td>
	<td>BEL</td>
	<td>1.HC</td>
	<td>GILBERT (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20494&CompetitionCodeInv=1&EditionID=891349&SeasonID=486&EventID=10635&EventPhaseID=891773&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris-Camembert</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>COQUARD (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;Apr-13&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22038&CompetitionCodeInv=1&EditionID=891476&SeasonID=486&EventID=12146&EventPhaseID=891891&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour du Maroc</a></td>
	<td>MAR</td>
	<td>2.2</td>
	<td>LOUBET (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Apr-13&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26618&CompetitionCodeInv=1&EditionID=891735&SeasonID=486&EventID=12146&EventPhaseID=892111&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Volta Ciclística Internacional do Rio Grande do Sul</a></td>
	<td>BRA</td>
	<td>2.2</td>
	<td>RODRIGUEZ (CHI)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;Apr-13&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22690&CompetitionCodeInv=1&EditionID=891521&SeasonID=486&EventID=12146&EventPhaseID=891931&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Circuit des Ardennes International</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>WISNIOWSKI (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23819&CompetitionCodeInv=1&EditionID=891600&SeasonID=486&EventID=10635&EventPhaseID=891990&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Banja Luka-Belgrade II</a></td>
	<td>SRB</td>
	<td>1.2</td>
	<td>STEVIC (SRB)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20503&CompetitionCodeInv=1&EditionID=891355&SeasonID=486&EventID=10635&EventPhaseID=891777&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Klasika Primavera de Amorebieta</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>BILBAO (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20502&CompetitionCodeInv=1&EditionID=888103&SeasonID=486&EventID=10635&EventPhaseID=888140&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris - Roubaix</a></td>
	<td>FRA</td>
	<td>UWT</td>
	<td>TERPSTRA (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>07&nbsp;Apr-12&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20493&CompetitionCodeInv=1&EditionID=888101&SeasonID=486&EventID=12146&EventPhaseID=888138&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta Ciclista al Pais Vasco</a></td>
	<td>ESP</td>
	<td>UWT</td>
	<td>CONTADOR VELASCO (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Apr-12&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26097&CompetitionCodeInv=1&EditionID=891700&SeasonID=486&EventID=12146&EventPhaseID=892078&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Mzansi Tour</a></td>
	<td>RSA</td>
	<td>2.2</td>
	<td>JANSE VAN RENSBURG (RSA)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23823&CompetitionCodeInv=1&EditionID=891601&SeasonID=486&EventID=10635&EventPhaseID=891991&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Banja Luka Belgrade I</a></td>
	<td>BIH</td>
	<td>1.2</td>
	<td>OTONICAR (SLO)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22959&CompetitionCodeInv=1&EditionID=891550&SeasonID=486&EventID=10635&EventPhaseID=891947&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Edil C</a></td>
	<td>ITA</td>
	<td>1.2</td>
	<td>VACCHER (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20499&CompetitionCodeInv=1&EditionID=891352&SeasonID=486&EventID=10635&EventPhaseID=891775&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix Cerami</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>PETACCHI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Apr-11&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20498&CompetitionCodeInv=1&EditionID=891351&SeasonID=486&EventID=12146&EventPhaseID=891774&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Circuit Cycliste Sarthe - Pays de la Loire</a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>NAVARDAUSKAS (LTU)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21416&CompetitionCodeInv=1&EditionID=888206&SeasonID=486&EventID=10635&EventPhaseID=888260&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Scheldeprijs</a></td>
	<td>BEL</td>
	<td>1.HC</td>
	<td>KITTEL (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Apr-06&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23315&CompetitionCodeInv=1&EditionID=891565&SeasonID=486&EventID=12146&EventPhaseID=891960&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix of Sochi</a></td>
	<td>RUS</td>
	<td>2.2</td>
	<td>ZAKARIN (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Apr-06&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23593&CompetitionCodeInv=1&EditionID=891586&SeasonID=486&EventID=12146&EventPhaseID=891977&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">The Maha Chackri Sirindhon's Cup "Tour of Thailand"</a></td>
	<td>THA</td>
	<td>2.2</td>
	<td>NAKAJIMA (JPN)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;Apr-06&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21975&CompetitionCodeInv=1&EditionID=891474&SeasonID=486&EventID=12146&EventPhaseID=891889&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Le Triptyque des Monts et Châteaux</a></td>
	<td>BEL</td>
	<td>2.2</td>
	<td>DOULL (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20490&CompetitionCodeInv=1&EditionID=888100&SeasonID=486&EventID=10635&EventPhaseID=888136&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ronde van Vlaanderen / Tour des Flandres</a></td>
	<td>BEL</td>
	<td>UWT</td>
	<td>CANCELLARA (SUI)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20889&CompetitionCodeInv=1&EditionID=891434&SeasonID=486&EventID=10635&EventPhaseID=891852&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta Ciclista a la Rioja</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>MATTHEWS (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21255&CompetitionCodeInv=1&EditionID=891442&SeasonID=486&EventID=10635&EventPhaseID=891859&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Gran Premio Miguel Indurain</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>VALVERDE BELMONTE (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20500&CompetitionCodeInv=1&EditionID=891353&SeasonID=486&EventID=10635&EventPhaseID=891776&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Volta Limburg Classic</a></td>
	<td>NED</td>
	<td>1.1</td>
	<td>HOFLAND (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21517&CompetitionCodeInv=1&EditionID=891447&SeasonID=486&EventID=10635&EventPhaseID=891863&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Route Adélie de Vitré</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>COQUARD (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Apr-03&nbsp;Apr&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20487&CompetitionCodeInv=1&EditionID=888182&SeasonID=486&EventID=12146&EventPhaseID=888235&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">VDK-Driedaagse De Panne-Koksijde</a></td>
	<td>BEL</td>
	<td>2.HC</td>
	<td>VAN KEIRSBULCK (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>24&nbsp;Mar-30&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20586&CompetitionCodeInv=1&EditionID=888111&SeasonID=486&EventID=12146&EventPhaseID=888148&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Volta Ciclista a Catalunya</a></td>
	<td>ESP</td>
	<td>UWT</td>
	<td>RODRIGUEZ OLIVER (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>24&nbsp;Mar-30&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20480&CompetitionCodeInv=1&EditionID=891346&SeasonID=486&EventID=12146&EventPhaseID=891771&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Normandie</a></td>
	<td>FRA</td>
	<td>2.2</td>
	<td>KUENG (SUI)</td>
</tr>
<tr valign="top">
	<td><nobr>26&nbsp;Mar-30&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20528&CompetitionCodeInv=1&EditionID=891366&SeasonID=486&EventID=12146&EventPhaseID=891785&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Volta ao Alentejo/Crédito Agricola Costa Azul</a></td>
	<td>POR</td>
	<td>2.2</td>
	<td>BARBERO CUESTA (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Mar-30&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20482&CompetitionCodeInv=1&EditionID=891347&SeasonID=486&EventID=12146&EventPhaseID=891772&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Settimana Internazionale Coppi e Bartali</a></td>
	<td>ITA</td>
	<td>2.1</td>
	<td>KENNAUGH (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;Mar-30&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20885&CompetitionCodeInv=1&EditionID=888204&SeasonID=486&EventID=12146&EventPhaseID=888258&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Critérium International</a></td>
	<td>FRA</td>
	<td>2.HC</td>
	<td>PERAUD (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>30&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20497&CompetitionCodeInv=1&EditionID=888102&SeasonID=486&EventID=10635&EventPhaseID=888139&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Gent-Wevelgem In Flanders Fields</a></td>
	<td>BEL</td>
	<td>UWT</td>
	<td>DEGENKOLB (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26627&CompetitionCodeInv=1&EditionID=891744&SeasonID=486&EventID=10635&EventPhaseID=892120&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Criterium International de Blida</a></td>
	<td>ALG</td>
	<td>1.2</td>
	<td>AMICABILE (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25351&CompetitionCodeInv=1&EditionID=891663&SeasonID=486&EventID=10635&EventPhaseID=892047&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Circuit International d'Alger</a></td>
	<td>ALG</td>
	<td>1.2</td>
	<td>LAGAB (ALG)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20483&CompetitionCodeInv=1&EditionID=888099&SeasonID=486&EventID=10635&EventPhaseID=888135&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">E3 Harelbeke</a></td>
	<td>BEL</td>
	<td>UWT</td>
	<td>SAGAN (SVK)</td>
</tr>
<tr valign="top">
	<td><nobr>24&nbsp;Mar-27&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26624&CompetitionCodeInv=1&EditionID=891741&SeasonID=486&EventID=12146&EventPhaseID=892117&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour International de Constantine</a></td>
	<td>ALG</td>
	<td>2.2</td>
	<td>BELYKH (RUS)</td>
</tr>
<tr valign="top">
	<td><nobr>26&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20481&CompetitionCodeInv=1&EditionID=888180&SeasonID=486&EventID=10635&EventPhaseID=888233&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Dwars door Vlaanderen / A travers la Flandre</a></td>
	<td>BEL</td>
	<td>1.HC</td>
	<td>TERPSTRA (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>23&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20477&CompetitionCodeInv=1&EditionID=888098&SeasonID=486&EventID=10635&EventPhaseID=888134&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Milano - Sanremo</a></td>
	<td>ITA</td>
	<td>UWT</td>
	<td>KRISTOFF (NOR)</td>
</tr>
<tr valign="top">
	<td><nobr>23&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20478&CompetitionCodeInv=1&EditionID=891345&SeasonID=486&EventID=10635&EventPhaseID=891770&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Cholet - Pays De Loire</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>VAN ASBROECK (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26622&CompetitionCodeInv=1&EditionID=891739&SeasonID=486&EventID=10635&EventPhaseID=892115&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Criterium International de Setif</a></td>
	<td>ALG</td>
	<td>1.2</td>
	<td>LAHSAINI (MAR)</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23158&CompetitionCodeInv=1&EditionID=891554&SeasonID=486&EventID=10635&EventPhaseID=891950&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Classic Loire Atlantique</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>GOUGEARD (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Mar-21&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26623&CompetitionCodeInv=1&EditionID=891740&SeasonID=486&EventID=12146&EventPhaseID=892116&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour International de Setif</a></td>
	<td>ALG</td>
	<td>2.2</td>
	<td>LEBAS (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25178&CompetitionCodeInv=1&EditionID=891655&SeasonID=486&EventID=10635&EventPhaseID=892037&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Handzame Classic</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>MEZGEC (SLO)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23186&CompetitionCodeInv=1&EditionID=891557&SeasonID=486&EventID=10635&EventPhaseID=891952&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">GP Nobili Rubinetterie-Coppa Papà Carlo-Coppa Città di Stresa</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>PONZI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20775&CompetitionCodeInv=1&EditionID=891424&SeasonID=486&EventID=10635&EventPhaseID=891843&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Nokere Koerse - Danilith Classic</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>DE HAES (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar-18&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23430&CompetitionCodeInv=1&EditionID=891576&SeasonID=486&EventID=12146&EventPhaseID=891968&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour du Cameroun</a></td>
	<td>CMR</td>
	<td>2.2</td>
	<td>CRAVEN (NAM)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Mar-18&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20471&CompetitionCodeInv=1&EditionID=888097&SeasonID=486&EventID=12146&EventPhaseID=888133&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tirreno - Adriatico</a></td>
	<td>ITA</td>
	<td>UWT</td>
	<td>CONTADOR VELASCO (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Mar-18&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26103&CompetitionCodeInv=1&EditionID=891701&SeasonID=486&EventID=12146&EventPhaseID=932554&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour International de Blida</a></td>
	<td>ALG</td>
	<td>2.2</td>
	<td>EGERZEIGZAARHKA (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar-16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20469&CompetitionCodeInv=1&EditionID=888096&SeasonID=486&EventID=12146&EventPhaseID=888132&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris - Nice</a></td>
	<td>FRA</td>
	<td>UWT</td>
	<td>BETANCUR GOMEZ (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Mar-16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22206&CompetitionCodeInv=1&EditionID=891488&SeasonID=486&EventID=12146&EventPhaseID=891905&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Istarsko proljece - Istrian Spring Trophy</a></td>
	<td>CRO</td>
	<td>2.2</td>
	<td>NIELSEN (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21966&CompetitionCodeInv=1&EditionID=891473&SeasonID=486&EventID=10635&EventPhaseID=891888&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris-Troyes</a></td>
	<td>FRA</td>
	<td>1.2</td>
	<td>TRONET (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21963&CompetitionCodeInv=1&EditionID=891471&SeasonID=486&EventID=10635&EventPhaseID=891886&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Kattekoers</a></td>
	<td>BEL</td>
	<td>1.2</td>
	<td>WISNIOWSKI (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=24841&CompetitionCodeInv=1&EditionID=891640&SeasonID=486&EventID=10635&EventPhaseID=892024&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Energiewacht Dwars door Drenthe</a></td>
	<td>NED</td>
	<td>1.1</td>
	<td>PONZI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20772&CompetitionCodeInv=1&EditionID=891423&SeasonID=486&EventID=10635&EventPhaseID=891842&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Omloop van het Waasland</a></td>
	<td>BEL</td>
	<td>1.2</td>
	<td>NAPOLITANO (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21574&CompetitionCodeInv=1&EditionID=891454&SeasonID=486&EventID=10635&EventPhaseID=891870&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Albert Achterhes Pet Ronde van Drenthe</a></td>
	<td>NED</td>
	<td>1.1</td>
	<td>DE HAES (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>14&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26626&CompetitionCodeInv=1&EditionID=891743&SeasonID=486&EventID=10635&EventPhaseID=892119&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix d'Oran</a></td>
	<td>ALG</td>
	<td>1.2</td>
	<td>BARBARI (ALG)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar-13&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21982&CompetitionCodeInv=1&EditionID=891475&SeasonID=486&EventID=12146&EventPhaseID=891890&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Taiwan</a></td>
	<td>TPE</td>
	<td>2.1</td>
	<td>DI GREGORIO (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar-13&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21630&CompetitionCodeInv=1&EditionID=891462&SeasonID=486&EventID=12146&EventPhaseID=891878&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour d'Algérie</a></td>
	<td>ALG</td>
	<td>2.2</td>
	<td>DEBESAY (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;Mar-09&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20741&CompetitionCodeInv=1&EditionID=894244&SeasonID=486&EventID=12146&EventPhaseID=894245&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta Mexico</a></td>
	<td>MEX</td>
	<td>2.2</td>
	<td>VILLEGAS (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>07&nbsp;Mar-09&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=22365&CompetitionCodeInv=1&EditionID=891498&SeasonID=486&EventID=12146&EventPhaseID=891918&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Driedaagse van West-Vlaanderen</a></td>
	<td>BEL</td>
	<td>2.1</td>
	<td>JOEAAR (EST)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21964&CompetitionCodeInv=1&EditionID=891472&SeasonID=486&EventID=10635&EventPhaseID=891887&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Rabobank Dorpenomloop Rucphen</a></td>
	<td>NED</td>
	<td>1.2</td>
	<td>CARBEL SVENDGAARD (DEN)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23333&CompetitionCodeInv=1&EditionID=891573&SeasonID=486&EventID=10635&EventPhaseID=891965&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Porec Trophy - Trofej Porec</a></td>
	<td>CRO</td>
	<td>1.2</td>
	<td>AVERIN (UKR)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20710&CompetitionCodeInv=1&EditionID=891408&SeasonID=486&EventID=10635&EventPhaseID=891826&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Roma Maxima</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>VALVERDE BELMONTE (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20468&CompetitionCodeInv=1&EditionID=891344&SeasonID=486&EventID=10635&EventPhaseID=891769&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix de la Ville de Lillers Souvenir Bruno Comini</a></td>
	<td>FRA</td>
	<td>1.2</td>
	<td>TRONET (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Mar-16&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23266&CompetitionCodeInv=1&EditionID=895981&SeasonID=486&EventID=10636&EventPhaseID=895983&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Juegos Suramericanos Santiago</a></td>
	<td>CHI</td>
	<td>JR</td>
	<td>AFFONSO (BRA)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Feb-08&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20457&CompetitionCodeInv=1&EditionID=888178&SeasonID=486&EventID=12146&EventPhaseID=888231&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Le Tour de Langkawi</a></td>
	<td>MAS</td>
	<td>2.HC</td>
	<td>POURSEYEDIGOLAKHOUR (IRI)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20763&CompetitionCodeInv=1&EditionID=891419&SeasonID=486&EventID=10635&EventPhaseID=891838&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Ster van Zwolle</a></td>
	<td>NED</td>
	<td>1.2</td>
	<td>LINDEMAN (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26625&CompetitionCodeInv=1&EditionID=891742&SeasonID=486&EventID=10635&EventPhaseID=892118&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Criterium International d'Alger</a></td>
	<td>ALG</td>
	<td>1.2</td>
	<td>RABOU (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23854&CompetitionCodeInv=1&EditionID=891602&SeasonID=486&EventID=10635&EventPhaseID=891992&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Strade Bianche</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>KWIATKOWSKI (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20650&CompetitionCodeInv=1&EditionID=891395&SeasonID=486&EventID=10635&EventPhaseID=891815&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">G.P. Camaiore</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>ULISSI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20769&CompetitionCodeInv=1&EditionID=891422&SeasonID=486&EventID=10635&EventPhaseID=891841&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Le Samyn</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>VANTOMME (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26223&CompetitionCodeInv=1&EditionID=891719&SeasonID=486&EventID=10635&EventPhaseID=892095&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofej Umag - Umag Trophy</a></td>
	<td>CRO</td>
	<td>1.2</td>
	<td>MUGERLI (SLO)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26109&CompetitionCodeInv=1&EditionID=891704&SeasonID=486&EventID=10635&EventPhaseID=892082&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">La Drôme Classic</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>BARDET (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25146&CompetitionCodeInv=1&EditionID=888218&SeasonID=486&EventID=10635&EventPhaseID=888272&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Les challenges de la Marche verte - GP Al Massira</a></td>
	<td>MAR</td>
	<td>1.2</td>
	<td>ALEKSIEV  (BUL)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;Feb-02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23475&CompetitionCodeInv=1&EditionID=906555&SeasonID=486&EventID=10635&EventPhaseID=906557&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - NAM RR</a></td>
	<td>NAM</td>
	<td>CN</td>
	<td>SEIBEB (NAM)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23564&CompetitionCodeInv=1&EditionID=906546&SeasonID=486&EventID=10635&EventPhaseID=906548&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - PAR RR</a></td>
	<td>PAR</td>
	<td>CN</td>
	<td>GROBENSTIEG (PAR)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22679&CompetitionCodeInv=1&EditionID=891516&SeasonID=486&EventID=10635&EventPhaseID=891927&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">G.P. Città di Lugano</a></td>
	<td>SUI</td>
	<td>1.1</td>
	<td>FINETTO (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20460&CompetitionCodeInv=1&EditionID=891342&SeasonID=486&EventID=10635&EventPhaseID=891767&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Kuurne-Brussel-Kuurne</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>BOONEN (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20444&CompetitionCodeInv=1&EditionID=888177&SeasonID=486&EventID=10635&EventPhaseID=888230&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Clasica de Almeria</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>BENNETT (IRL)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20458&CompetitionCodeInv=1&EditionID=888179&SeasonID=486&EventID=10635&EventPhaseID=888232&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Omloop Het Nieuwsblad Elite</a></td>
	<td>BEL</td>
	<td>1.HC</td>
	<td>STANNARD (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20463&CompetitionCodeInv=1&EditionID=891343&SeasonID=486&EventID=10635&EventPhaseID=891768&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta Ciclista a Murcia</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>VALVERDE BELMONTE (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23949&CompetitionCodeInv=1&EditionID=891612&SeasonID=486&EventID=10635&EventPhaseID=891999&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Classic Sud Ardèche - Souvenir Francis Delpech</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>VACHON (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25147&CompetitionCodeInv=1&EditionID=888219&SeasonID=486&EventID=10635&EventPhaseID=888273&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Les challenges de la Marche verte - GP Oued Eddahab</a></td>
	<td>MAR</td>
	<td>1.2</td>
	<td>LAHSAINI (MAR)</td>
</tr>
<tr valign="top">
	<td><nobr>28&nbsp;Feb-02&nbsp;Mar&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=23475&CompetitionCodeInv=1&EditionID=906555&SeasonID=486&EventID=10636&EventPhaseID=906556&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">NCh - NAM ITT</a></td>
	<td>NAM</td>
	<td>CN</td>
	<td>DROBISCH (NAM)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Feb-27&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20449&CompetitionCodeInv=1&EditionID=891340&SeasonID=486&EventID=12146&EventPhaseID=891765&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta Independencia Nacional</a></td>
	<td>DOM</td>
	<td>2.2</td>
	<td>SANCHEZ ANZOLA (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>27&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25148&CompetitionCodeInv=1&EditionID=888220&SeasonID=486&EventID=10635&EventPhaseID=888274&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Les challenges de la Marche verte - GP Sakia El Hamra</a></td>
	<td>MAR</td>
	<td>1.2</td>
	<td>ABELOUACHE (MAR)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;Feb-23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=24617&CompetitionCodeInv=1&EditionID=888216&SeasonID=486&EventID=12146&EventPhaseID=888270&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Oman</a></td>
	<td>OMA</td>
	<td>2.HC</td>
	<td>FROOME (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Feb-23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20445&CompetitionCodeInv=1&EditionID=891338&SeasonID=486&EventID=12146&EventPhaseID=891763&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta a Andalucia - Ruta Ciclista Del Sol</a></td>
	<td>ESP</td>
	<td>2.1</td>
	<td>VALVERDE BELMONTE (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>19&nbsp;Feb-23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20900&CompetitionCodeInv=1&EditionID=891435&SeasonID=486&EventID=12146&EventPhaseID=891853&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Volta ao Algarve</a></td>
	<td>POR</td>
	<td>2.1</td>
	<td>KWIATKOWSKI (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Feb-23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20451&CompetitionCodeInv=1&EditionID=891341&SeasonID=486&EventID=12146&EventPhaseID=891766&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour Cycliste International du Haut Var-matin</a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>BETANCUR GOMEZ (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26607&CompetitionCodeInv=1&EditionID=891725&SeasonID=486&EventID=10635&EventPhaseID=892101&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">GP Izola - Butan plin</a></td>
	<td>SLO</td>
	<td>1.2</td>
	<td>DELLE STELLE (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Feb-23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20759&CompetitionCodeInv=1&EditionID=905945&SeasonID=486&EventID=10635&EventPhaseID=905955&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Oceania Cycling Championships RR</a></td>
	<td>AUS</td>
	<td>CC</td>
	<td>DURBRIDGE (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20447&CompetitionCodeInv=1&EditionID=891339&SeasonID=486&EventID=10635&EventPhaseID=891764&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Laigueglia</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>SERPA PEREZ (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Feb-23&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20759&CompetitionCodeInv=1&EditionID=905945&SeasonID=486&EventID=10636&EventPhaseID=905950&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Oceania Cycling Championships ITT</a></td>
	<td>AUS</td>
	<td>CC</td>
	<td>COOPER (NZL)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Feb-16&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23444&CompetitionCodeInv=1&EditionID=891577&SeasonID=486&EventID=12146&EventPhaseID=891969&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour do Brasil Volta Ciclística de São Paulo-Internacional</a></td>
	<td>BRA</td>
	<td>2.2</td>
	<td>NAZARET (BRA)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Feb-16&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20442&CompetitionCodeInv=1&EditionID=891337&SeasonID=486&EventID=12146&EventPhaseID=891762&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour Méditerranéen Cycliste Professionnel</a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>CUMMINGS (GBR)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Feb-14&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23215&CompetitionCodeInv=1&EditionID=888210&SeasonID=486&EventID=12146&EventPhaseID=888264&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Qatar</a></td>
	<td>QAT</td>
	<td>2.HC</td>
	<td>TERPSTRA (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20439&CompetitionCodeInv=1&EditionID=891336&SeasonID=486&EventID=10635&EventPhaseID=891761&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Platja de Muro</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>MEERSMAN (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22894&CompetitionCodeInv=1&EditionID=891549&SeasonID=486&EventID=10635&EventPhaseID=891946&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Deià</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>KWIATKOWSKI (POL)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25811&CompetitionCodeInv=1&EditionID=891687&SeasonID=486&EventID=10635&EventPhaseID=892069&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Migjorn</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>MODOLO (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Feb-09&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20437&CompetitionCodeInv=1&EditionID=891334&SeasonID=486&EventID=12146&EventPhaseID=891759&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Etoile de Bessèges</a></td>
	<td>FRA</td>
	<td>2.1</td>
	<td>LUDVIGSSON (SWE)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Feb-09&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20726&CompetitionCodeInv=1&EditionID=891415&SeasonID=486&EventID=12146&EventPhaseID=891833&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Jayco Herald Sun Tour</a></td>
	<td>AUS</td>
	<td>2.1</td>
	<td>CLARKE (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>09&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20438&CompetitionCodeInv=1&EditionID=891335&SeasonID=486&EventID=10635&EventPhaseID=891760&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Trofeo Palma</a></td>
	<td>ESP</td>
	<td>1.1</td>
	<td>MODOLO (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Feb-09&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22001&CompetitionCodeInv=1&EditionID=906561&SeasonID=486&EventID=10635&EventPhaseID=906570&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National d'Afrique du Sud RR</a></td>
	<td>RSA</td>
	<td>CN</td>
	<td>MEINTJES (RSA)</td>
</tr>
<tr valign="top">
	<td><nobr>05&nbsp;Feb-08&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26614&CompetitionCodeInv=1&EditionID=891731&SeasonID=486&EventID=12146&EventPhaseID=892107&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Dubai Tour</a></td>
	<td>UAE</td>
	<td>2.1</td>
	<td>PHINNEY (USA)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Feb-09&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22001&CompetitionCodeInv=1&EditionID=906561&SeasonID=486&EventID=10636&EventPhaseID=906566&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National d'Afrique du Sud ITT</a></td>
	<td>RSA</td>
	<td>CN</td>
	<td>IMPEY (RSA)</td>
</tr>
<tr valign="top">
	<td><nobr>29&nbsp;Jan-02&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21609&CompetitionCodeInv=1&EditionID=888285&SeasonID=486&EventID=12146&EventPhaseID=888286&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">New Zealand Cycle Classic</a></td>
	<td>NZL</td>
	<td>2.2</td>
	<td>VINK (NZL)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20436&CompetitionCodeInv=1&EditionID=891333&SeasonID=486&EventID=10635&EventPhaseID=891758&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand Prix Cycliste la Marseillaise</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>VAN BILSEN (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Feb&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21515&CompetitionCodeInv=1&EditionID=891446&SeasonID=486&EventID=10635&EventPhaseID=891862&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">G.P. Costa degli Etruschi</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>PONZI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Jan-26&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23817&CompetitionCodeInv=1&EditionID=888213&SeasonID=486&EventID=12146&EventPhaseID=888267&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de San Luis</a></td>
	<td>ARG</td>
	<td>2.1</td>
	<td>QUINTANA ROJAS (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>21&nbsp;Jan-26&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21608&CompetitionCodeInv=1&EditionID=888118&SeasonID=486&EventID=12146&EventPhaseID=888155&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Santos Tour Down Under</a></td>
	<td>AUS</td>
	<td>UWT</td>
	<td>GERRANS (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Jan-19&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21524&CompetitionCodeInv=1&EditionID=888207&SeasonID=486&EventID=12146&EventPhaseID=888261&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta al Tachira en Bicicleta</a></td>
	<td>VEN</td>
	<td>2.2</td>
	<td>BRICENO (VEN)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Jan-19&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23171&CompetitionCodeInv=1&EditionID=888209&SeasonID=486&EventID=12146&EventPhaseID=888263&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">La Tropicale Amissa Bongo</a></td>
	<td>GAB</td>
	<td>2.1</td>
	<td>BERHANE (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Jan-12&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21466&CompetitionCodeInv=1&EditionID=904897&SeasonID=486&EventID=10635&EventPhaseID=904902&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National de Nouvelle-Zelande RR</a></td>
	<td>NZL</td>
	<td>CN</td>
	<td>ROULSTON (NZL)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Jan-12&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20751&CompetitionCodeInv=1&EditionID=904890&SeasonID=486&EventID=10635&EventPhaseID=904896&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National d'Australie RR</a></td>
	<td>AUS</td>
	<td>CN</td>
	<td>GERRANS (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Jan-12&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=21466&CompetitionCodeInv=1&EditionID=904897&SeasonID=486&EventID=10636&EventPhaseID=904900&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National de Nouvelle-Zelande ITT</a></td>
	<td>NZL</td>
	<td>CN</td>
	<td>GUNMAN (NZL)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Jan-12&nbsp;Jan&nbsp;2014</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20751&CompetitionCodeInv=1&EditionID=904890&SeasonID=486&EventID=10636&EventPhaseID=904893&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Championnat National d'Australie ITT</a></td>
	<td>AUS</td>
	<td>CN</td>
	<td>HEPBURN (AUS)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;Dec-29&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20748&CompetitionCodeInv=1&EditionID=888202&SeasonID=486&EventID=12146&EventPhaseID=888255&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta kolbi a Costa Rica</a></td>
	<td>CRC</td>
	<td>2.2</td>
	<td>ROJAS VILLEGAS (CRC)</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=24995&CompetitionCodeInv=1&EditionID=902183&SeasonID=486&EventID=10635&EventPhaseID=902184&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">CFI International race 3, Dehli</a></td>
	<td>IND</td>
	<td>1.2</td>
	<td>ROSDI (MAS)</td>
</tr>
<tr valign="top">
	<td><nobr>18&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25596&CompetitionCodeInv=1&EditionID=902185&SeasonID=486&EventID=10635&EventPhaseID=902186&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">CFI International race 2, Jaipur</a></td>
	<td>IND</td>
	<td>1.2</td>
	<td>MUHD SHAIFUL (MAS)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=24618&CompetitionCodeInv=1&EditionID=902181&SeasonID=486&EventID=10635&EventPhaseID=902182&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">CFI International race 1, Mumbai</a></td>
	<td>IND</td>
	<td>1.2</td>
	<td>MARZUKI (MAS)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Dec-18&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=22749&CompetitionCodeInv=1&EditionID=889511&SeasonID=484&EventID=10636&EventPhaseID=889513&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Sea Games Myanmar</a></td>
	<td>MYA</td>
	<td>JR</td>
	<td>GALEDO (PHI)</td>
</tr>
<tr valign="top">
	<td><nobr>04&nbsp;Dec-07&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26593&CompetitionCodeInv=1&EditionID=888229&SeasonID=486&EventID=12146&EventPhaseID=888283&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Al Zubarah</a></td>
	<td>QAT</td>
	<td>2.2</td>
	<td>MIRZA BANIHAMMAD (UAE)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Dec-05&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20758&CompetitionCodeInv=1&EditionID=888203&SeasonID=486&EventID=10635&EventPhaseID=888256&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Champ. Continentaux Afrique RR</a></td>
	<td>EGY</td>
	<td>CC</td>
	<td>TESFOM OKUBAMARIAM (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Dec-05&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20758&CompetitionCodeInv=1&EditionID=888203&SeasonID=486&EventID=10636&EventPhaseID=888257&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Champ. Continentaux Afrique ITT</a></td>
	<td>EGY</td>
	<td>CC</td>
	<td>TEKLEHAIMANOT (ERI)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Dec-05&nbsp;Dec&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20758&CompetitionCodeInv=1&EditionID=888203&SeasonID=486&EventID=10637&EventPhaseID=888284&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Champ. Continentaux Afrique TTT</a></td>
	<td>EGY</td>
	<td>CC</td>
	<td>ERITREA</td>
</tr>
<tr valign="top">
	<td><nobr>22&nbsp;Nov-25&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26592&CompetitionCodeInv=1&EditionID=888228&SeasonID=486&EventID=12146&EventPhaseID=888282&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Sharjah International Cycling Tour</a></td>
	<td>UAE</td>
	<td>2.2</td>
	<td>VAN UDEN (NZL)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;Nov-24&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=24552&CompetitionCodeInv=1&EditionID=888215&SeasonID=486&EventID=12146&EventPhaseID=888269&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Rwanda</a></td>
	<td>RWA</td>
	<td>2.2</td>
	<td>GIRDLESTONE (RSA)</td>
</tr>
<tr valign="top">
	<td><nobr>16&nbsp;Nov-18&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26065&CompetitionCodeInv=1&EditionID=888223&SeasonID=486&EventID=12146&EventPhaseID=888277&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Fuzhou</a></td>
	<td>CHN</td>
	<td>2.2</td>
	<td>EMAMI (IRI)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26591&CompetitionCodeInv=1&EditionID=888227&SeasonID=486&EventID=10635&EventPhaseID=888281&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Nanjing</a></td>
	<td>CHN</td>
	<td>1.2</td>
	<td>KANKOVSKY (CZE)</td>
</tr>
<tr valign="top">
	<td><nobr>01&nbsp;Nov-10&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=24019&CompetitionCodeInv=1&EditionID=888214&SeasonID=486&EventID=12146&EventPhaseID=888268&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Vuelta a Bolivia</a></td>
	<td>BOL</td>
	<td>2.2</td>
	<td>MORENO HERNANDEZ (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Nov-10&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=25116&CompetitionCodeInv=1&EditionID=888217&SeasonID=486&EventID=12146&EventPhaseID=888271&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Taihu Lake</a></td>
	<td>CHN</td>
	<td>2.1</td>
	<td>METLUSHENKO (UKR)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20745&CompetitionCodeInv=1&EditionID=888201&SeasonID=486&EventID=10635&EventPhaseID=888254&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Okinawa</a></td>
	<td>JPN</td>
	<td>1.2</td>
	<td>HATSUYAMA (JPN)</td>
</tr>
<tr valign="top">
	<td><nobr>02&nbsp;Nov-05&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=26067&CompetitionCodeInv=1&EditionID=888224&SeasonID=486&EventID=12146&EventPhaseID=888278&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Banyuwangi Tour de Ijen</a></td>
	<td>INA</td>
	<td>2.2</td>
	<td>POURSEYEDIGOLAKHOUR (IRI)</td>
</tr>
<tr valign="top">
	<td><nobr>25&nbsp;Oct-03&nbsp;Nov&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20747&CompetitionCodeInv=1&EditionID=885728&SeasonID=486&EventID=12146&EventPhaseID=885729&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour du Faso</a></td>
	<td>BUR</td>
	<td>2.2</td>
	<td>NIKIEMA (BUR)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Oct-28&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=21533&CompetitionCodeInv=1&EditionID=885724&SeasonID=486&EventID=12146&EventPhaseID=885725&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Hainan</a></td>
	<td>CHN</td>
	<td>2.HC</td>
	<td>HOFLAND (NED)</td>
</tr>
<tr valign="top">
	<td><nobr>17&nbsp;Oct-20&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23742&CompetitionCodeInv=1&EditionID=885720&SeasonID=486&EventID=12146&EventPhaseID=885721&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Grand prix Chantal Biya</a></td>
	<td>CMR</td>
	<td>2.2</td>
	<td>NGUE (CMR)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20738&CompetitionCodeInv=1&EditionID=885722&SeasonID=486&EventID=10635&EventPhaseID=885723&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Japan Cup Cycle Road Race</a></td>
	<td>JPN</td>
	<td>1.HC</td>
	<td>BAUER (NZL)</td>
</tr>
<tr valign="top">
	<td><nobr>20&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20734&CompetitionCodeInv=1&EditionID=822622&SeasonID=484&EventID=10636&EventPhaseID=823104&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Chrono des Nations</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>MARTIN (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>11&nbsp;Oct-15&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=23301&CompetitionCodeInv=1&EditionID=810700&SeasonID=484&EventID=12146&EventPhaseID=810701&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Beijing</a></td>
	<td>CHN</td>
	<td>UWT</td>
	<td>INTXAUSTI ELORRIAGA (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>15&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20842&CompetitionCodeInv=1&EditionID=822640&SeasonID=484&EventID=10635&EventPhaseID=823126&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Nationale Sluitingprijs - Putte - Kapellen</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>DEBUSSCHERE (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20723&CompetitionCodeInv=1&EditionID=822617&SeasonID=484&EventID=10635&EventPhaseID=823099&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris - Tours Elite</a></td>
	<td>FRA</td>
	<td>1.HC</td>
	<td>DEGENKOLB (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>13&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20704&CompetitionCodeInv=1&EditionID=822608&SeasonID=484&EventID=10635&EventPhaseID=823090&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Gran Premio Bruno Beghelli</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>DUQUE (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>12&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20717&CompetitionCodeInv=1&EditionID=822614&SeasonID=484&EventID=10635&EventPhaseID=823096&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Giro dell'Emilia</a></td>
	<td>ITA</td>
	<td>1.HC</td>
	<td>ULISSI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20716&CompetitionCodeInv=1&EditionID=822613&SeasonID=484&EventID=10635&EventPhaseID=823095&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Gran Premio Città di Peccioli - Coppa Sabatini</a></td>
	<td>ITA</td>
	<td>1.1</td>
	<td>ULISSI (ITA)</td>
</tr>
<tr valign="top">
	<td><nobr>10&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20725&CompetitionCodeInv=1&EditionID=822618&SeasonID=484&EventID=10635&EventPhaseID=823100&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Paris-Bourges</a></td>
	<td>FRA</td>
	<td>1.1</td>
	<td>DEGENKOLB (GER)</td>
</tr>
<tr valign="top">
	<td><nobr>08&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20563&CompetitionCodeInv=1&EditionID=822571&SeasonID=484&EventID=10635&EventPhaseID=823055&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Binche-Tournai-Binche/Mémorial Frank Vandenbroucke</a></td>
	<td>BEL</td>
	<td>1.1</td>
	<td>JANSE VAN RENSBURG (RSA)</td>
</tr>
<tr valign="top">
	<td><nobr>03&nbsp;Oct-06&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=resultoverview&SportID=102&CompetitionID=20626&CompetitionCodeInv=1&EditionID=822582&SeasonID=484&EventID=12146&EventPhaseID=823066&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de l'Eurométropole</a></td>
	<td>BEL</td>
	<td>2.1</td>
	<td>DEBUSSCHERE (BEL)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20521&CompetitionCodeInv=1&EditionID=822550&SeasonID=484&EventID=10635&EventPhaseID=823034&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour de Vendée</a></td>
	<td>FRA</td>
	<td>1.HC</td>
	<td>BOUHANNI (FRA)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=20732&CompetitionCodeInv=1&EditionID=810698&SeasonID=484&EventID=10635&EventPhaseID=810699&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Il Lombardia</a></td>
	<td>ITA</td>
	<td>UWT</td>
	<td>RODRIGUEZ OLIVER (ESP)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=25576&CompetitionCodeInv=1&EditionID=885716&SeasonID=486&EventID=10635&EventPhaseID=885717&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tobago Cycling Classic</a></td>
	<td>TRI</td>
	<td>1.2</td>
	<td>RAMIREZ BERNAL (COL)</td>
</tr>
<tr valign="top">
	<td><nobr>06&nbsp;Oct&nbsp;2013</nobr></td>
	<td><a href="/asp/redirect/uci.asp?Page=result&SportID=102&CompetitionID=26584&CompetitionCodeInv=1&EditionID=885718&SeasonID=486&EventID=10635&EventPhaseID=885719&GenderID=1&ClassID=1&Phase1ID=-1&Detail=1&DerivedEventPhaseID=-1&Ranking=0">Tour of Almaty</a></td>
	<td>KAZ</td>
	<td>1.2</td>
	<td>IGLINSKY (KAZ)</td>
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
