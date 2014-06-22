# -*- coding: utf-8 -*-
general_response = '''

<html>
<head>
<title>Sports Result</title>
<script type="text/javascript" language="JavaScript">
	<!--
	function Submit2SamePage(oForm) {
		oForm.elements[0].value = 19006;
		oForm.action = 'TheASP.asp';
		oForm.submit();
	};
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakeEventPhase() { this.length=1; return this; }
	EventPhaseID = new MakeEventPhase(); EventPhase = new MakeEventPhase();
	EventPhaseID[0]=888147; EventPhase[0]="Individual";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhase1() { this.length=10; return this; }
	Phase1ID = new MakePhase1(); Phase1 = new MakePhase1();
	Phase1ID[0]=0; Phase1[0]="Final";
	Phase1ID[1]=898892; Phase1[1]="Stage 9";
	Phase1ID[2]=898891; Phase1[2]="Stage 8";
	Phase1ID[3]=898890; Phase1[3]="Stage 7";
	Phase1ID[4]=898889; Phase1[4]="Stage 6";
	Phase1ID[5]=898888; Phase1[5]="Stage 5";
	Phase1ID[6]=898887; Phase1[6]="Stage 4";
	Phase1ID[7]=898886; Phase1[7]="Stage 3";
	Phase1ID[8]=898885; Phase1[8]="Stage 2";
	Phase1ID[9]=898884; Phase1[9]="Stage 1";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhase2() { this.length=1; return this; }
	Phase2ID = new MakePhase2(); Phase2 = new MakePhase2();
	Phase2ID[0]=0; Phase2[0]="";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhase3() { this.length=1; return this; }
	Phase3ID = new MakePhase3(); Phase3 = new MakePhase3();
	Phase3ID[0]=0; Phase3[0]="";
	// -->
</script>
<script type="text/javascript" language="JavaScript">
	<!--
	function MakePhaseClassification() { this.length=4; return this; }
	PhaseClassificationID = new MakePhaseClassification(); PhaseClassification = new MakePhaseClassification();
	PhaseClassificationID[0]=905947; PhaseClassification[0]="Result";
	PhaseClassificationID[1]=1006057; PhaseClassification[1]="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Points";
	PhaseClassificationID[2]=1006058; PhaseClassification[2]="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Mountain";
	PhaseClassificationID[3]=1006060; PhaseClassification[3]="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Team";
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
	<span class="crumblepad_header">Results - Cycling - Road 2014 </span>
	<br/> <br/>
	Men
	<img src="/images/icons/bullet.gif">
	Elite
	<img src="/images/icons/bullet.gif">
	Tour de Suisse
	(SUI/UWT)
	<br>
	<div class="subtitlered">
		14 Jun-22 Jun 2014 - General classification:
	</div>
</div>


</td><td valign="top" width=120>
<div id="seasoncombo" style="float:right;display:inline;padding-top:5px;">
<script type="text/javascript">
fSeasonDropdown(102, 486, 1, 1, 0, 1, 2, 0, 8)
</script>
</div>
<div style="float:right;padding-top:10px;">

<form name="TheASPform0" action="TheASP.asp" method="get">
<table cellpadding="0" border="0"><tr>
<input name="PageID" type="hidden" value="19006" />
<input name="TaalCode" type="hidden" value="2" />
<input name="StyleID" type="hidden" value="0" />
<input name="Cache" type="hidden" value="8" />
<input name="SportID" type="hidden" value="102" />
<input name="CompetitionID" type="hidden" value="20583" />
<input name="EditionID" type="hidden" value="888110" />
<input name="SeasonID" type="hidden" value="486" />
<input name="EventID" type="hidden" value="12146" />
<input name="GenderID" type="hidden" value="1" />
<input name="ClassID" type="hidden" value="1" />
<input name="PhaseStatusCode" type="hidden" value="262280" />
<input name="EventPhaseID" type="hidden" value="888147" />
<input name="Phase1ID" type="hidden" value="0" />
<input name="Phase2ID" type="hidden" value="0" />
<input name="Phase3ID" type="hidden" value="0" />
<input name="PhaseClassificationID" type="hidden" value="905947" />
<input name="Detail" type="hidden" value="1" />
<input name="Ranking" type="hidden" value="0" />
<input name="DerivedEventPhaseID" type="hidden" value="-1" />
<input name="S00" type="hidden" value="1" /><input name="S01" type="hidden" value="2" /><input name="S02" type="hidden" value="3" /><td></form></div></td></tr></table>
</div>
</td></tr></table><div style="clear:both"></div>
<div class="main_menu_container">
 <div class="content_item_container">
<div class="menu_item_white_border">
	<div class="menu_item_active">
		<div class="menu_item_tekst">
			<a href="/asp/redirect/uci.asp?page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventPhaseID=888147&EventID=12146&ContainerEventID=12146&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&PhaseClassificationID=905947&DerivedEventPhaseID=-1&detail=1&ranking=0">General</a>
		</div>
	</div>
</div>


<div class="menu_item_white_border">
	<div class="menu_item">
		<div class="menu_item_tekst">
			<a href="/asp/redirect/uci.asp?page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventPhaseID=888147&EventID=12146&ContainerEventID=12146&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&PhaseClassificationID=1006057&DerivedEventPhaseID=-1&detail=1&ranking=0">Points</a>
		</div>
	</div>
</div>


<div class="menu_item_white_border">
	<div class="menu_item">
		<div class="menu_item_tekst">
			<a href="/asp/redirect/uci.asp?page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventPhaseID=888147&EventID=12146&ContainerEventID=12146&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&PhaseClassificationID=1006058&DerivedEventPhaseID=-1&detail=1&ranking=0">Mountain</a>
		</div>
	</div>
</div>


<div class="menu_item_white_border">
	<div class="menu_item">
		<div class="menu_item_tekst">
			<a href="/asp/redirect/uci.asp?page=result&SportID=102&CompetitionID=20583&CompetitionCodeInv=1&EditionID=888110&SeasonID=486&EventPhaseID=888147&EventID=12146&ContainerEventID=12146&GenderID=1&ClassID=1&Phase1ID=0&Phase2ID=0&Phase3ID=0&PhaseClassificationID=1006060&DerivedEventPhaseID=-1&detail=1&ranking=0">Team time</a>
		</div>
	</div>
</div>


</div></div>

<table width="100%" border="0" cellspacing="0" cellpadding="3" class="datatable">
<tr>
	<td class="caption">Rank</td>
	<td class="caption">Name</td>
	<td class="caption">Nat.</td>
	<td class="caption">Team</td>
	<td class="caption" align="center">Age*</td>
	<td class="caption" align="right">Result</td>
</tr>
<tr valign="top">
	<td>1 </td>
	<td>Rui Alberto FARIA DA COSTA</td>
	<td>POR</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">28</td>
	<td align="right">33:08:35</td>
</tr>
<tr valign="top">
	<td>2 </td>
	<td>Mathias FRANK</td>
	<td>SUI</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">28</td>
	<td align="right">+33</td>
</tr>
<tr valign="top">
	<td>3 </td>
	<td>Bauke MOLLEMA</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">28</td>
	<td align="right">+50</td>
</tr>
<tr valign="top">
	<td>4 </td>
	<td>Tony MARTIN</td>
	<td>GER</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">29</td>
	<td align="right">+1:13</td>
</tr>
<tr valign="top">
	<td>5 </td>
	<td>Tom DUMOULIN</td>
	<td>NED</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">24</td>
	<td align="right">+2:04</td>
</tr>
<tr valign="top">
	<td>6 </td>
	<td>Steve MORABITO</td>
	<td>SUI</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">31</td>
	<td align="right">+2:47</td>
</tr>
<tr valign="top">
	<td>7 </td>
	<td>Davide FORMOLO</td>
	<td>ITA</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">22</td>
	<td align="right">+3:00</td>
</tr>
<tr valign="top">
	<td>8 </td>
	<td>Roman KREUZIGER</td>
	<td>CZE</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">28</td>
	<td align="right">+3:03</td>
</tr>
<tr valign="top">
	<td>9 </td>
	<td>Janier Alexis ACEVEDO COLLE</td>
	<td>COL</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">29</td>
	<td align="right">+3:20</td>
</tr>
<tr valign="top">
	<td>10 </td>
	<td>Eros CAPECCHI</td>
	<td>ITA</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">28</td>
	<td align="right">+3:46</td>
</tr>
<tr valign="top">
	<td>11 </td>
	<td>Cadel EVANS</td>
	<td>AUS</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">37</td>
	<td align="right">+4:07</td>
</tr>
<tr valign="top">
	<td>12 </td>
	<td>Sergio PARDILLA BELLON</td>
	<td>ESP</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">30</td>
	<td align="right">+4:10</td>
</tr>
<tr valign="top">
	<td>13 </td>
	<td>Laurens TEN DAM</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">34</td>
	<td align="right">+4:55</td>
</tr>
<tr valign="top">
	<td>14 </td>
	<td>Rafael VALLS FERRI</td>
	<td>ESP</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">27</td>
	<td align="right">+5:27</td>
</tr>
<tr valign="top">
	<td>15 </td>
	<td>Thibaut PINOT</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">24</td>
	<td align="right">+5:45</td>
</tr>
<tr valign="top">
	<td>16 </td>
	<td>Jhoan Esteban  CHAVES RUBIO</td>
	<td>COL</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">24</td>
	<td align="right">+5:54</td>
</tr>
<tr valign="top">
	<td>17 </td>
	<td>Thomas DEGAND</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">28</td>
	<td align="right">+6:04</td>
</tr>
<tr valign="top">
	<td>18 </td>
	<td>Marcel WYSS</td>
	<td>SUI</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">28</td>
	<td align="right">+6:29</td>
</tr>
<tr valign="top">
	<td>19 </td>
	<td>Arnold JEANNESSON</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">28</td>
	<td align="right">+6:56</td>
</tr>
<tr valign="top">
	<td>20 </td>
	<td>Kevin SEELDRAEYERS</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">28</td>
	<td align="right">+7:15</td>
</tr>
<tr valign="top">
	<td>21 </td>
	<td>Oliver ZAUGG</td>
	<td>SUI</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">33</td>
	<td align="right">+8:57</td>
</tr>
<tr valign="top">
	<td>22 </td>
	<td>Andre Fernando S. Martins CARDOSO</td>
	<td>POR</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">30</td>
	<td align="right">+9:12</td>
</tr>
<tr valign="top">
	<td>23 </td>
	<td>Stef CLEMENT</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">32</td>
	<td align="right">+10:35</td>
</tr>
<tr valign="top">
	<td>24 </td>
	<td>Tomasz MARCZYNSKI</td>
	<td>POL</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">30</td>
	<td align="right">+10:43</td>
</tr>
<tr valign="top">
	<td>25 </td>
	<td>Sergei CHERNETSKI</td>
	<td>RUS</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">24</td>
	<td align="right">+11:28</td>
</tr>
<tr valign="top">
	<td>26 </td>
	<td>Louis MEINTJES</td>
	<td>RSA</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">22</td>
	<td align="right">+11:32</td>
</tr>
<tr valign="top">
	<td>27 </td>
	<td>Steven KRUIJSWIJK</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">27</td>
	<td align="right">+13:59</td>
</tr>
<tr valign="top">
	<td>28 </td>
	<td>Enrico GASPAROTTO</td>
	<td>ITA</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">32</td>
	<td align="right">+14:38</td>
</tr>
<tr valign="top">
	<td>29 </td>
	<td>Andy SCHLECK</td>
	<td>LUX</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">29</td>
	<td align="right">+15:07</td>
</tr>
<tr valign="top">
	<td>30 </td>
	<td>Warren BARGUIL</td>
	<td>FRA</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">23</td>
	<td align="right">+15:30</td>
</tr>
<tr valign="top">
	<td>31 </td>
	<td>Tosh VAN DER SANDE</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">24</td>
	<td align="right">+17:09</td>
</tr>
<tr valign="top">
	<td>32 </td>
	<td>Javier MORENO BAZAN</td>
	<td>ESP</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">30</td>
	<td align="right">+20:28</td>
</tr>
<tr valign="top">
	<td>33 </td>
	<td>Michael SCHÄR</td>
	<td>SUI</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">28</td>
	<td align="right">+20:31</td>
</tr>
<tr valign="top">
	<td>34 </td>
	<td>Johann TSCHOPP</td>
	<td>SUI</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">32</td>
	<td align="right">+20:56</td>
</tr>
<tr valign="top">
	<td>35 </td>
	<td>Francis DE GREEF</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">29</td>
	<td align="right">+23:18</td>
</tr>
<tr valign="top">
	<td>36 </td>
	<td>Alexandr KOLOBNEV</td>
	<td>RUS</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">33</td>
	<td align="right">+23:41</td>
</tr>
<tr valign="top">
	<td>37 </td>
	<td>Jose Rodolfo SERPA PEREZ</td>
	<td>COL</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">35</td>
	<td align="right">+23:48</td>
</tr>
<tr valign="top">
	<td>38 </td>
	<td>Christian KNEES</td>
	<td>GER</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">33</td>
	<td align="right">+24:09</td>
</tr>
<tr valign="top">
	<td>39 </td>
	<td>Georg PREIDLER</td>
	<td>AUT</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">24</td>
	<td align="right">+24:33</td>
</tr>
<tr valign="top">
	<td>40 </td>
	<td>Jose Joaquin ROJAS GIL</td>
	<td>ESP</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">29</td>
	<td align="right">+25:19</td>
</tr>
<tr valign="top">
	<td>41 </td>
	<td>Benjamin KING</td>
	<td>USA</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">25</td>
	<td align="right">+26:02</td>
</tr>
<tr valign="top">
	<td>42 </td>
	<td>Bjorn THURAU</td>
	<td>GER</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">26</td>
	<td align="right">+26:27</td>
</tr>
<tr valign="top">
	<td>43 </td>
	<td>Jon IZAGUIRRE INSAUSTI</td>
	<td>ESP</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">25</td>
	<td align="right">+26:28</td>
</tr>
<tr valign="top">
	<td>44 </td>
	<td>Silvan DILLIER</td>
	<td>SUI</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">24</td>
	<td align="right">+27:58</td>
</tr>
<tr valign="top">
	<td>45 </td>
	<td>Tom Jelte SLAGTER</td>
	<td>NED</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">25</td>
	<td align="right">+27:59</td>
</tr>
<tr valign="top">
	<td>46 </td>
	<td>Jérémy ROY</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">31</td>
	<td align="right">+32:02</td>
</tr>
<tr valign="top">
	<td>47 </td>
	<td>Joseph Lloyd DOMBROWSKI</td>
	<td>USA</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">23</td>
	<td align="right">+32:03</td>
</tr>
<tr valign="top">
	<td>48 </td>
	<td>Philip DEIGNAN</td>
	<td>IRL</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">31</td>
	<td align="right">+32:28</td>
</tr>
<tr valign="top">
	<td>49 </td>
	<td>Ruben PLAZA MOLINA</td>
	<td>ESP</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">34</td>
	<td align="right">+33:28</td>
</tr>
<tr valign="top">
	<td>50 </td>
	<td>Reto HOLLENSTEIN</td>
	<td>SUI</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">29</td>
	<td align="right">+34:37</td>
</tr>
<tr valign="top">
	<td>51 </td>
	<td>Marek RUTKIEWICZ</td>
	<td>POL</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">33</td>
	<td align="right">+37:58</td>
</tr>
<tr valign="top">
	<td>52 </td>
	<td>Davide REBELLIN</td>
	<td>ITA</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">43</td>
	<td align="right">+38:09</td>
</tr>
<tr valign="top">
	<td>53 </td>
	<td>Nino SCHURTER</td>
	<td>SUI</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">28</td>
	<td align="right">+38:16</td>
</tr>
<tr valign="top">
	<td>54 </td>
	<td>Branislau SAMOILAU</td>
	<td>BLR</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">29</td>
	<td align="right">+39:57</td>
</tr>
<tr valign="top">
	<td>55 </td>
	<td>Jonathan FUMEAUX</td>
	<td>SUI</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">26</td>
	<td align="right">+41:03</td>
</tr>
<tr valign="top">
	<td>56 </td>
	<td>Francesco GAVAZZI</td>
	<td>ITA</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">30</td>
	<td align="right">+41:04</td>
</tr>
<tr valign="top">
	<td>57 </td>
	<td>Aliaksandr KUCHYNSKI</td>
	<td>BLR</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">35</td>
	<td align="right">+41:29</td>
</tr>
<tr valign="top">
	<td>58 </td>
	<td>Matthieu LADAGNOUS</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">30</td>
	<td align="right">+42:55</td>
</tr>
<tr valign="top">
	<td>59 </td>
	<td>Nathan BROWN</td>
	<td>USA</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">23</td>
	<td align="right">+44:00</td>
</tr>
<tr valign="top">
	<td>60 </td>
	<td>Alexandre PICHOT</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">31</td>
	<td align="right">+44:59</td>
</tr>
<tr valign="top">
	<td>61 </td>
	<td>Maxime MEDEREL</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">34</td>
	<td align="right">+45:29</td>
</tr>
<tr valign="top">
	<td>62 </td>
	<td>Lawson CRADDOCK</td>
	<td>USA</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">22</td>
	<td align="right">+45:47</td>
</tr>
<tr valign="top">
	<td>63 </td>
	<td>Nelson Filipe SANTOS SIMOES OLIVEIRA</td>
	<td>POR</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">25</td>
	<td align="right">+46:23</td>
</tr>
<tr valign="top">
	<td>64 </td>
	<td>Laurent DIDIER</td>
	<td>LUX</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">30</td>
	<td align="right">+46:47</td>
</tr>
<tr valign="top">
	<td>65 </td>
	<td>Martin KOHLER</td>
	<td>SUI</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">29</td>
	<td align="right">+49:03</td>
</tr>
<tr valign="top">
	<td>66 </td>
	<td>Martin ELMIGER</td>
	<td>SUI</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">36</td>
	<td align="right">+49:14</td>
</tr>
<tr valign="top">
	<td>67 </td>
	<td>Johan VAN SUMMEREN</td>
	<td>BEL</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">33</td>
	<td align="right">+49:24</td>
</tr>
<tr valign="top">
	<td>68 </td>
	<td>Peter SAGAN</td>
	<td>SVK</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">24</td>
	<td align="right">+50:06</td>
</tr>
<tr valign="top">
	<td>69 </td>
	<td>Matteo TOSATTO</td>
	<td>ITA</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">40</td>
	<td align="right">+50:35</td>
</tr>
<tr valign="top">
	<td>70 </td>
	<td>Linus GERDEMANN</td>
	<td>GER</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">32</td>
	<td align="right">+51:48</td>
</tr>
<tr valign="top">
	<td>71 </td>
	<td>Koen DE KORT</td>
	<td>NED</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">32</td>
	<td align="right">+51:53</td>
</tr>
<tr valign="top">
	<td>72 </td>
	<td>Danilo WYSS</td>
	<td>SUI</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">29</td>
	<td align="right">+52:01</td>
</tr>
<tr valign="top">
	<td>73 </td>
	<td>Cristiano SALERNO</td>
	<td>ITA</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">29</td>
	<td align="right">+52:21</td>
</tr>
<tr valign="top">
	<td>74 </td>
	<td>Lukasz OWSIAN</td>
	<td>POL</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">24</td>
	<td align="right">+53:39</td>
</tr>
<tr valign="top">
	<td>75 </td>
	<td>Sep VANMARCKE</td>
	<td>BEL</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">26</td>
	<td align="right">+53:59</td>
</tr>
<tr valign="top">
	<td>76 </td>
	<td>Marcus BURGHARDT</td>
	<td>GER</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">31</td>
	<td align="right">+54:19</td>
</tr>
<tr valign="top">
	<td>77 </td>
	<td>Sébastien MINARD</td>
	<td>FRA</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">32</td>
	<td align="right">+1:00:46</td>
</tr>
<tr valign="top">
	<td>78 </td>
	<td>Lawrence WARBASSE</td>
	<td>USA</td>
	<td><!--BMC--><span title="BMC RACING TEAM">BMC</span></td>
	<td align="center">24</td>
	<td align="right">+1:01:57</td>
</tr>
<tr valign="top">
	<td>79 </td>
	<td>Anthony ROUX</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">27</td>
	<td align="right">+1:02:28</td>
</tr>
<tr valign="top">
	<td>80 </td>
	<td>Michael ALBASINI</td>
	<td>SUI</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">34</td>
	<td align="right">+1:03:28</td>
</tr>
<tr valign="top">
	<td>81 </td>
	<td>Cédric PINEAU</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">29</td>
	<td align="right">+1:05:29</td>
</tr>
<tr valign="top">
	<td>82 </td>
	<td>Simon CLARKE</td>
	<td>AUS</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">28</td>
	<td align="right">+1:05:53</td>
</tr>
<tr valign="top">
	<td>83 </td>
	<td>Thomas LEEZER</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">29</td>
	<td align="right">+1:07:56</td>
</tr>
<tr valign="top">
	<td>84 </td>
	<td>Sander ARMEE</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">29</td>
	<td align="right">+1:09:45</td>
</tr>
<tr valign="top">
	<td>85 </td>
	<td>Manuele BOARO</td>
	<td>ITA</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">27</td>
	<td align="right">+1:10:48</td>
</tr>
<tr valign="top">
	<td>86 </td>
	<td>Matteo TRENTIN</td>
	<td>ITA</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">25</td>
	<td align="right">+1:11:58</td>
</tr>
<tr valign="top">
	<td>87 </td>
	<td>Laurens DE VREESE</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">26</td>
	<td align="right">+1:12:08</td>
</tr>
<tr valign="top">
	<td>88 </td>
	<td>Giovanni BERNAUDEAU</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">31</td>
	<td align="right">+1:12:28</td>
</tr>
<tr valign="top">
	<td>89 </td>
	<td>Rohan DENNIS</td>
	<td>AUS</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">24</td>
	<td align="right">+1:12:43</td>
</tr>
<tr valign="top">
	<td>90 </td>
	<td>Grégory RAST</td>
	<td>SUI</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">34</td>
	<td align="right">+1:13:24</td>
</tr>
<tr valign="top">
	<td>91 </td>
	<td>Frederik VEUCHELEN</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">36</td>
	<td align="right">+1:15:30</td>
</tr>
<tr valign="top">
	<td>92 </td>
	<td>Daniele BENNATI</td>
	<td>ITA</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">34</td>
	<td align="right">+1:17:06</td>
</tr>
<tr valign="top">
	<td>93 </td>
	<td>Valentin IGLINSKIY</td>
	<td>KAZ</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">30</td>
	<td align="right">+1:18:40</td>
</tr>
<tr valign="top">
	<td>94 </td>
	<td>Heinrich HAUSSLER</td>
	<td>AUS</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">30</td>
	<td align="right">+1:21:08</td>
</tr>
<tr valign="top">
	<td>95 </td>
	<td>Fabio SABATINI</td>
	<td>ITA</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">29</td>
	<td align="right">+1:22:18</td>
</tr>
<tr valign="top">
	<td>96 </td>
	<td>Guillaume BOIVIN</td>
	<td>CAN</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">25</td>
	<td align="right">+1:22:54</td>
</tr>
<tr valign="top">
	<td>97 </td>
	<td>Gatis SMUKULIS</td>
	<td>LAT</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">27</td>
	<td align="right">+1:24:41</td>
</tr>
<tr valign="top">
	<td>98 </td>
	<td>Alexander PORSEV</td>
	<td>RUS</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">28</td>
	<td align="right">+1:26:20</td>
</tr>
<tr valign="top">
	<td>99 </td>
	<td>Chris Anker SÖRENSEN</td>
	<td>DEN</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">30</td>
	<td align="right">+1:26:38</td>
</tr>
<tr valign="top">
	<td>100 </td>
	<td>Alexander KRISTOFF</td>
	<td>NOR</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">27</td>
	<td align="right">+1:29:04</td>
</tr>
<tr valign="top">
	<td>101 </td>
	<td>Bryan COQUARD</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">22</td>
	<td align="right">+1:29:16</td>
</tr>
<tr valign="top">
	<td>102 </td>
	<td>Edward KING</td>
	<td>USA</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">31</td>
	<td align="right">+1:29:35</td>
</tr>
<tr valign="top">
	<td>103 </td>
	<td>Maciej PATERSKI</td>
	<td>POL</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">28</td>
	<td align="right">+1:30:11</td>
</tr>
<tr valign="top">
	<td>104 </td>
	<td>Jaco VENTER</td>
	<td>RSA</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">27</td>
	<td align="right">+1:30:16</td>
</tr>
<tr valign="top">
	<td>105 </td>
	<td>Christophe KERN</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">33</td>
	<td align="right">+1:32:46</td>
</tr>
<tr valign="top">
	<td>106 </td>
	<td>Michael MORKOV</td>
	<td>DEN</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">29</td>
	<td align="right">+1:33:36</td>
</tr>
<tr valign="top">
	<td>107 </td>
	<td>Yohann GENE</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">33</td>
	<td align="right">+1:34:42</td>
</tr>
<tr valign="top">
	<td>108 </td>
	<td>Jay Robert THOMSON</td>
	<td>RSA</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">28</td>
	<td align="right">+1:39:58</td>
</tr>
<tr valign="top">
	<td>109 </td>
	<td>Fredrik Carl Wilhelm KESSIAKOFF</td>
	<td>SWE</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">34</td>
	<td align="right">+1:40:10</td>
</tr>
<tr valign="top">
	<td>110 </td>
	<td>Vladimir ISAICHEV</td>
	<td>RUS</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">28</td>
	<td align="right">+1:41:20</td>
</tr>
<tr valign="top">
	<td>111 </td>
	<td>Jacopo GUARNIERI</td>
	<td>ITA</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">27</td>
	<td align="right">+1:42:01</td>
</tr>
<tr valign="top">
	<td>112 </td>
	<td>Sam BEWLEY</td>
	<td>NZL</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">27</td>
	<td align="right">+1:42:33</td>
</tr>
<tr valign="top">
	<td>113 </td>
	<td>Lloyd MONDORY</td>
	<td>FRA</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">32</td>
	<td align="right">+1:43:21</td>
</tr>
<tr valign="top">
	<td>114 </td>
	<td>Geoffrey SOUPE</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">26</td>
	<td align="right">+1:43:27</td>
</tr>
<tr valign="top">
	<td>115 </td>
	<td>Ramon SINKELDAM</td>
	<td>NED</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">25</td>
	<td align="right">+1:44:53</td>
</tr>
<tr valign="top">
	<td>116 </td>
	<td>Sébastien TURGOT</td>
	<td>FRA</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">30</td>
	<td align="right">+1:46:40</td>
</tr>
<tr valign="top">
	<td>117 </td>
	<td>Martin VELITS</td>
	<td>SVK</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">29</td>
	<td align="right">+1:50:46</td>
</tr>
<tr valign="top">
	<td>118 </td>
	<td>Marco HALLER</td>
	<td>AUT</td>
	<td><!--KAT--><span title="TEAM KATUSHA">KAT</span></td>
	<td align="center">23</td>
	<td align="right">+1:50:54</td>
</tr>
<tr valign="top">
	<td>119 </td>
	<td>Laurent MANGEL</td>
	<td>FRA</td>
	<td><!--FDJ--><span title="FDJ.FR">FDJ</span></td>
	<td align="center">33</td>
	<td align="right">+1:51:54</td>
</tr>
<tr valign="top">
	<td>120 </td>
	<td>Roger KLUGE</td>
	<td>GER</td>
	<td><!--IAM--><span title="IAM CYCLING">IAM</span></td>
	<td align="center">28</td>
	<td align="right">+1:52:22</td>
</tr>
<tr valign="top">
	<td>121 </td>
	<td>Andrea PALINI</td>
	<td>ITA</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">25</td>
	<td align="right">+1:54:25</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Valerio AGNOLI</td>
	<td>ITA</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Davide APPOLLONIO</td>
	<td>ITA</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Jérôme BAUGNIES</td>
	<td>BEL</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Tom BOONEN</td>
	<td>BEL</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">34</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Vegard BREEN</td>
	<td>NOR</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Matti BRESCHEL</td>
	<td>DEN</td>
	<td><!--TCS--><span title="TINKOFF-SAXO">TCS</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Matthew BUSCHE</td>
	<td>USA</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Fabian CANCELLARA</td>
	<td>SUI</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">33</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Mattia CATTANEO</td>
	<td>ITA</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Mark CAVENDISH</td>
	<td>GBR</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Gerald CIOLEK</td>
	<td>GER</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">28</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Thomas DANIELSON</td>
	<td>USA</td>
	<td><!--GRS--><span title="GARMIN SHARP">GRS</span></td>
	<td align="center">36</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>John DEGENKOLB</td>
	<td>GER</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Kenny DE HAES</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Stijn DEVOLDER</td>
	<td>BEL</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">35</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Gert DOCKX</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Alex DOWSETT</td>
	<td>GBR</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Jimmy ENGOULVENT</td>
	<td>FRA</td>
	<td><!--EUC--><span title="TEAM EUROPCAR">EUC</span></td>
	<td align="center">35</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Marc GOOS</td>
	<td>NED</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Matthew Harley GOSS</td>
	<td>AUS</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">28</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Patrick GRETSCH</td>
	<td>GER</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Mathew HAYMAN</td>
	<td>AUS</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">36</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Sergio Luis HENAO MONTOYA</td>
	<td>COL</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Maxim IGLINSKY</td>
	<td>KAZ</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">33</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Jacques JANSE VAN RENSBURG</td>
	<td>RSA</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Peter KENNAUGH</td>
	<td>GBR</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Julian KERN</td>
	<td>GER</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Michel KREDER</td>
	<td>NED</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Pablo LASTRAS GARCIA</td>
	<td>ESP</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">38</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Juan Jose LOBATO DEL VALLE</td>
	<td>ESP</td>
	<td><!--MOV--><span title="MOVISTAR TEAM">MOV</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Jaroslaw MARYCZ</td>
	<td>POL</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Cameron MEYER</td>
	<td>AUS</td>
	<td><!--OGE--><span title="ORICA GREENEDGE">OGE</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Luka MEZGEC</td>
	<td>SLO</td>
	<td><!--GIA--><span title="TEAM GIANT-SHIMANO">GIA</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Sacha MODOLO</td>
	<td>ITA</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Maxime MONFORT</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">31</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Moreno MOSER</td>
	<td>ITA</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Domenico POZZOVIVO</td>
	<td>ITA</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">32</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Daniele RATTO</td>
	<td>ITA</td>
	<td><!--CAN--><span title="CANNONDALE">CAN</span></td>
	<td align="center">25</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Mark RENSHAW</td>
	<td>AUS</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">32</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Christophe RIBLON</td>
	<td>FRA</td>
	<td><!--ALM--><span title="AG2R LA MONDIALE">ALM</span></td>
	<td align="center">33</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Maximiliano Ariel RICHEZE</td>
	<td>ARG</td>
	<td><!--LAM--><span title="LAMPRE-MERIDA">LAM</span></td>
	<td align="center">31</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Luke ROWE</td>
	<td>GBR</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">24</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Frank SCHLECK</td>
	<td>LUX</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">34</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Mirko SELVAGGI</td>
	<td>ITA</td>
	<td><!--WGG--><span title="WANTY - GROUPE GOBERT">WGG</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Gert STEEGMANS</td>
	<td>BEL</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">34</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Ben SWIFT</td>
	<td>GBR</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Mateusz TACIAK</td>
	<td>POL</td>
	<td><!--CCC--><span title="CCC POLSAT POLKOWICE">CCC</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Daniel TEKLEHAIMANOT</td>
	<td>ERI</td>
	<td><!--MTN--><span title="MTN - QHUBEKA">MTN</span></td>
	<td align="center">26</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Niki TERPSTRA</td>
	<td>NED</td>
	<td><!--OPQ--><span title="OMEGA PHARMA - QUICK-STEP CYCLING TEAM">OPQ</span></td>
	<td align="center">30</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Ruslan TLEUBAYEV</td>
	<td>KAZ</td>
	<td><!--AST--><span title="ASTANA PRO TEAM">AST</span></td>
	<td align="center">27</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Jonas VANGENECHTEN</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">28</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Danny VAN POPPEL</td>
	<td>NED</td>
	<td><!--TFR--><span title="TREK FACTORY RACING">TFR</span></td>
	<td align="center">21</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Jelle VANENDERT</td>
	<td>BEL</td>
	<td><!--LTB--><span title="LOTTO BELISOL">LTB</span></td>
	<td align="center">29</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Bradley WIGGINS</td>
	<td>GBR</td>
	<td><!--SKY--><span title="TEAM SKY">SKY</span></td>
	<td align="center">34</td>
	<td align="right">&nbsp;</td>
</tr>
<tr valign="top">
	<td> </td>
	<td>Maarten WYNANTS</td>
	<td>BEL</td>
	<td><!--BEL--><span title="BELKIN-PRO CYCLING TEAM">BEL</span></td>
	<td align="center">32</td>
	<td align="right">&nbsp;</td>
</tr>
</table>
<table width="98%" border="0" cellspacing="0" cellpadding="2" class="datatablelegend">
<tr valign="top"><td colspan="2">Age*:&nbsp;according to UCI Regulations</td></tr>
</table>
</td><td width="5"><img src="/images/nix.gif" width="5" height="1"></td></tr></table>
<br /><img src="/images/libs/nix.gif" width=1  height=5 border=0>

</font>
</body>
</html>
'''
