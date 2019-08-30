-- MySQL dump 10.13  Distrib 5.7.17, for osx10.12 (x86_64)
--
-- Host: localhost    Database: db16
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add user',2,'add_user'),(5,'Can change user',2,'change_user'),(6,'Can delete user',2,'delete_user'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add artical',7,'add_artical'),(20,'Can change artical',7,'change_artical'),(21,'Can delete artical',7,'delete_artical'),(22,'Can add author',8,'add_author'),(23,'Can change author',8,'change_author'),(24,'Can delete author',8,'delete_author'),(25,'Can add user',9,'add_user'),(26,'Can change user',9,'change_user'),(27,'Can delete user',9,'delete_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_artical`
--

DROP TABLE IF EXISTS `blog_artical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_artical` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `text` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_artical_e8701ad4` (`user_id`),
  CONSTRAINT `blog_artical_user_id_fb73d246_fk_blog_user_id` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_artical`
--

LOCK TABLES `blog_artical` WRITE;
/*!40000 ALTER TABLE `blog_artical` DISABLE KEYS */;
INSERT INTO `blog_artical` VALUES (1,'长安号','2017-05-15','陕西一家肉类企业公司总经理朱维敬最近也很忙。整个5月上旬，西安港进口肉类口岸、陕西出入境检验检疫局、西安海关和西安国际港务区都在协调朱维敬一单50吨肉品的进口事宜。',1),(2,'教育部','2017-05-11','清晨，东方微曦，西安市东北20公里的新筑站已一片忙碌。此时，距离当地公务员上班的时间还有两小时。 不久之前，有媒体将西安与“中国第三城”联系在一起，其理由是作为中国文化代表之地，西安能抛却其他指标成为中国展示在世界的“第三城”。 文化毋庸置疑成为西安争夺“第三城”陕西省商务厅一名官员对此解读称，“长安号”货运班列贡献明显。而界面新闻记者也注意到，西安市2017年政府工作报告中，在“对外开放有了新突破”一节中，特别提及了“长安号”实现常态化运营的贡献。 除此之外不可忽略的是，“长安号”的开通为西安经济、贸易模式提供了更多的可能性。而在此之前，西安“不沿海、不沿边、不沿江”的内陆进出口贸易的劣势一直挥之不去。 陕西省商务厅为界面新闻记者提供了一个例子：不久之前，西安一家公司在蒙古国投资了一家烟厂，但全世界最好的烟丝产自津巴布韦，问题是津巴布韦货币不稳定，且管制较严。这名负责人就与陕西省商务厅对接，考虑在“长安号”的起点西安国际港务区内的保税区加工烟丝，然后通过“长安号”运往蒙古。',2),(3,'python进程','2017-05-02','考虑一个场景：浏览器，网易云音乐以及notepad++ 三个软件只能顺序执行是怎样一种场景呢？另外，假如有两个程序A和B，程序A在执行到一半的过程中，需要读取大量的数据输入（I/O操作），而此时CPU只能静静地等待任务A读取完数据才能继续执行，这样就白白浪费了CPU资源。你是不是已经想到在程序A读取数据的过程中，让程序B去执行，当程序A读取完数据之后，让程序B暂停。聪明，这当然没问题，但这里有一个关键词：切换。\n\n既然是切换，那么这就涉及到了状态的保存，状态的恢复，加上程序A与程序B所需要的系统资源（内存，硬盘，键盘等等）是不一样的。自然而然的就需要有一个东西去记录程序A和程序B分别需要什么资源，怎样去识别程序A和程序B等等(比如读书)。\n\n进程定义：\n\n进程就是一个程序在一个数据集上的一次动态执行过程。进程一般由程序、数据集、进程控制块三部分组成。我们编写的程序用来描述进程要完成哪些功能以及如何完成；数据集则是程序在执行过程中所需要使用的资源；进程控制块用来记录进程的外部特征，描述进程的执行变化过程，系统可以利用它来控制和管理进程，它是系统感知进程存在的唯一标志。\n\n举一例说明进程：\n想象一位有一手好厨艺的计算机科学家正在为他的女儿烘制生日蛋糕。他有做生日蛋糕的食谱，厨房里有所需的原料:面粉、鸡蛋、糖、香草汁等。在这个比喻中，做蛋糕的食谱就是程序(即用适当形式描述的算法)计算机科学家就是处理器(cpu)，而做蛋糕的各种原料就是输入数据。进程就是厨师阅读食谱、取来各种原料以及烘制蛋糕等一系列动作的总和。现在假设计算机科学家的儿子哭着跑了进来，说他的头被一只蜜蜂蛰了。计算机科学家就记录下他照着食谱做到哪儿了(保存进程的当前状态)，然后拿出一本急救手册，按照其中的指示处理蛰伤。这里，我们看到处理机从一个进程(做蛋糕)切换到另一个高优先级的进程(实施医疗救治)，每个进程拥有各自的程序(食谱和急救手册)。当蜜蜂蛰伤处理完之后，这位计算机科学家又回来做蛋糕，从他\n离开时的那一步继续做下去。',1),(4,'python线程','2017-05-01','线程的出现是为了降低上下文切换的消耗，提高系统的并发性，并突破一个进程只能干一样事的缺陷，使到进程内并发成为可能。\n\n假设，一个文本程序，需要接受键盘输入，将内容显示在屏幕上，还需要保存信息到硬盘中。若只有一个进程，势必造成同一时间只能干一样事的尴尬（当保存时，就不能通过键盘输入内容）。若有多个进程，每个进程负责一个任务，进程A负责接收键盘输入的任务，进程B负责将内容显示在屏幕上的任务，进程C负责保存内容到硬盘中的任务。这里进程A，B，C间的协作涉及到了进程通信问题，而且有共同都需要拥有的东西——-文本内容，不停的切换造成性能上的损失。若有一种机制，可以使任务A，B，C共享资源，这样上下文切换所需要保存和恢复的内容就少了，同时又可以减少通信所带来的性能损耗，那就好了。是的，这种机制就是线程。\n线程也叫轻量级进程，它是一个基本的CPU执行单元，也是程序执行过程中的最小单元，由线程ID、程序计数器、寄存器集合和堆栈共同组成。线程的引入减小了程序并发执行时的开销，提高了操作系统的并发性能。线程没有自己的系统资源。',1),(5,'git','2017-05-06','为什么要编写这个教程？因为我在学习Git的过程中，买过书，也在网上Google了一堆Git相关的文章和教程，但令人失望的是，这些教程不是难得令人发指，就是简单得一笔带过，或者，只支离破碎地介绍Git的某几个命令，还有直接从Git手册粘贴帮助文档的，总之，初学者很难找到一个由浅入深，学完后能立刻上手的Git教程。\n\n既然号称史上最浅显易懂的Git教程，那这个教程有什么让你怦然心动的特点呢？\n\n首先，本教程绝对面向初学者，没有接触过版本控制概念的读者也可以轻松入门，不必担心起步难度；\n\n其次，本教程实用性超强，边学边练，一点也不觉得枯燥。而且，你所学的Git命令是“充分且必要”的，掌握了这些东西，你就可以通过Git轻松地完成你的工作。',1),(6,'github','2017-05-01','本教程只会让你成为Git用户，不会让你成为Git专家。很多Git命令只有那些专家才明白（事实上我也不明白，因为我不是Git专家），但我保证这些命令可能你一辈子都不会用到。既然Git是一个工具，就没必要把时间浪费在那些“高级”但几乎永远不会用到的命令上。一旦你真的非用不可了，到时候再自行Google或者请教专家也未迟。\n\n如果你是一个开发人员，想用上这个世界上目前最先进的分布式版本控制系统，那么，赶快开始学习吧！',2),(10,'test','2017-05-04','但我保证这些命令可能你一辈子都不会用到。既然Git是一个工具，就没必要把时间浪费在那些“高级”但几乎永远不会用到的命令上。一旦你真的非用不可了，到时候再自行Google或者请教专家也未迟。 如果你是一个开发人员，想用上这个世界上目前最先进的分布式版本控制系统，那么，赶快开始学习吧！',1),(11,'test2','2017-05-12','但我保证这些命令可能你一辈子都不会用到。既然Git是一个工具，就没必要把时间浪费在那些“高级”但几乎永远不会用到的命令上。一旦你真的非用不可了，到时候再自行Google或者请教专家也未迟。 如果你是一个开发人员，，那么，赶快开始学习吧！',1),(12,'习近平','2017-05-03','习近平指出，今年是中阿建交45周年。中阿两国作为二十国集团成员和重要新兴市场国家，双方加强合作，不仅符合两国和两国人民根本利益，也有利于促进世界繁荣稳定。中阿双方要巩固政治共识，引领好两国关系发展方向，使两国合作成果更好惠及两国人民',1),(13,'一路','2017-05-10','习近平赞赏阿根廷支持并积极参与“一带一路”建设，强调拉美是21世纪海上丝绸之路的自然延伸。中方愿同拉美加强合作，包括在“一带一路”建设框架内实现中拉发展战略对接，促进共同发展，打造中拉命运共同体',2),(14,'一代','2017-05-15','马克里热烈祝贺刚刚闭幕的“一带一路”国际合作高峰论坛取得圆满成功。马克里表示，阿方致力于推动阿中全面战略伙伴关系深入发展。阿方坚持一个中国政策，愿本着相互尊重、相互信任的精神推进两国互利合作，增进两国人民相互理解，扩大双方共识。阿方愿同中方共同努力，推动贸易平衡发展，加强投资、金融、农业、科技、基础设施、旅游、人文、足球合作，深化拉美同中国关系，密切在国际事务中的沟通和协调。',2),(15,'文化','2017-05-08','两国元首共同见证了教育、文化、农业、质检、体育、投资、能源、铁路和金融等领域双边合作文件的签署。\n\n　　会谈前，习近平在人民大会堂东门外广场为马克里举行欢迎仪式。彭丽媛、王沪宁、栗战书、全国人大常委会副委员长陈昌智、杨洁篪、全国政协副主席王钦敏等出席。',2),(16,'您好','2017-01-01','1111111111111111111111111111111111111111111111111111111111111111111',1),(18,'早晨','2017-01-01','一天之际',1),(20,'FQ','2017-05-19','仅仅靠单一的关键字参数查询已经很难满足查询要求。此时Django为我们提供了F和Q查询：',1);
/*!40000 ALTER TABLE `blog_artical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_artical_author`
--

DROP TABLE IF EXISTS `blog_artical_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_artical_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `artical_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_artical_author_artical_id_fb80e7dd_uniq` (`artical_id`,`author_id`),
  KEY `blog_artical_author_author_id_1d1de88e_fk_blog_author_id` (`author_id`),
  CONSTRAINT `blog_artical_author_artical_id_50dc6521_fk_blog_artical_id` FOREIGN KEY (`artical_id`) REFERENCES `blog_artical` (`id`),
  CONSTRAINT `blog_artical_author_author_id_1d1de88e_fk_blog_author_id` FOREIGN KEY (`author_id`) REFERENCES `blog_author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_artical_author`
--

LOCK TABLES `blog_artical_author` WRITE;
/*!40000 ALTER TABLE `blog_artical_author` DISABLE KEYS */;
INSERT INTO `blog_artical_author` VALUES (1,1,1),(3,1,2),(2,2,2),(4,3,1),(5,4,1),(6,5,1),(7,6,2),(18,10,4),(8,11,1),(9,11,2),(10,12,1),(11,12,2),(12,13,1),(13,13,2),(14,14,1),(15,14,2),(16,15,1),(19,16,2),(23,18,4),(22,20,1);
/*!40000 ALTER TABLE `blog_artical_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_author`
--

DROP TABLE IF EXISTS `blog_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` varchar(3) NOT NULL,
  `city` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_author`
--

LOCK TABLES `blog_author` WRITE;
/*!40000 ALTER TABLE `blog_author` DISABLE KEYS */;
INSERT INTO `blog_author` VALUES (1,'莫言','53','长沙'),(2,'韩寒','33','北京'),(4,'雨果','88','巴黎');
/*!40000 ALTER TABLE `blog_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_user`
--

DROP TABLE IF EXISTS `blog_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `sex` varchar(2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_user`
--

LOCK TABLES `blog_user` WRITE;
/*!40000 ALTER TABLE `blog_user` DISABLE KEYS */;
INSERT INTO `blog_user` VALUES (1,'willian','123123','男'),(2,'alex','123123','女');
/*!40000 ALTER TABLE `blog_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(4,'auth','permission'),(2,'auth','user'),(7,'blog','artical'),(8,'blog','author'),(9,'blog','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-05-15 05:51:32.053802'),(2,'auth','0001_initial','2017-05-15 05:51:32.386621'),(3,'admin','0001_initial','2017-05-15 05:51:32.467969'),(4,'admin','0002_logentry_remove_auto_add','2017-05-15 05:51:32.505897'),(5,'contenttypes','0002_remove_content_type_name','2017-05-15 05:51:32.579127'),(6,'auth','0002_alter_permission_name_max_length','2017-05-15 05:51:32.616329'),(7,'auth','0003_alter_user_email_max_length','2017-05-15 05:51:32.670322'),(8,'auth','0004_alter_user_username_opts','2017-05-15 05:51:32.681680'),(9,'auth','0005_alter_user_last_login_null','2017-05-15 05:51:32.716233'),(10,'auth','0006_require_contenttypes_0002','2017-05-15 05:51:32.719542'),(11,'auth','0007_alter_validators_add_error_messages','2017-05-15 05:51:32.730402'),(12,'auth','0008_alter_user_username_max_length','2017-05-15 05:51:32.762686'),(13,'blog','0001_initial','2017-05-15 05:51:32.987124'),(14,'sessions','0001_initial','2017-05-15 05:51:33.031014');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-05-19 11:52:41
