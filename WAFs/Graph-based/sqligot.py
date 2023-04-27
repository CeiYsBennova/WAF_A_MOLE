import re
import os

PUNCTATION_SUB = [
	("&&", "AND"),
	("<", "LT"),
	("<=", "LTE"),
	("<>", "NEQ"),
	("!=", "NEQ"),
	("=", "EQ"),
	(">", "GT"),
	(">=", "GTE"),
	("<<", "LSL"),
	(">>", "RSL"),
	("<=>", "NULLEQ"),
	("||", "OR"),
	("/*", "CMTST"),
	("*/", "CMTEND"),
	("~", "TILDE"),
	("!", "EXCLAMATION"),
	("@", "ATR"),
	("#", "HASH"),
	("$", "DOLLAR"),
	("%", "PERCENT"),
	("^", "CARET"),
	("&", "BITAND"),
	("|", "BITOR"),
	("*", "STAR"),
	("(", "LPNR"),
	(")", "RPRN"),
	("{", "RCBR"),
	("}", "LCBR"),
	("[", "LSQBR"),
	("]", "RSQBR"),
	("\\", "BSLASH"),
	(":", "COLON"),
	(";", "SEMICOLON"),
	('"', "DQUT"),
	("'", "SQUOT"),
	(",", "COMMA"),
	(".", "PERIOD"),
	("?", "QMARK"),
	("/", "FSLASH"),
]
SYMBOLS = [
	"ACCESSIBLE",
	"ACTION",
	"ADD",
	"ADMIN",
	"AFTER",
	"AGAINST",
	"AGGREGATE",
	"ALL",
	"ALGORITHM",
	"ALTER",
	"ALWAYS",
	"ANALYZE",
	"AND",
	"ANY",
	"AS",
	"ASC",
	"ASCII",
	"ASENSITIVE",
	"AT",
	"AUDIT",
	"AUTHORS",
	"AUTO_INCREMENT",
	"AUTOEXTEND_SIZE",
	"AUTO",
	"AVG",
	"AVG_ROW_LENGTH",
	"BACKUP",
	"BEFORE",
	"BEGIN",
	"BETWEEN",
	"BIGINT",
	"BINARY",
	"BINLOG",
	"BIT",
	"BLOB",
	"BLOCK",
	"BOOL",
	"BOOLEAN",
	"BOTH",
	"BTREE",
	"BY",
	"BYTE",
	"CACHE",
	"CALL",
	"CASCADE",
	"CASCADED",
	"CASE",
	"CATALOG_NAME",
	"CHAIN",
	"CHANGE",
	"CHANGED",
	"CHAR",
	"CHARACTER",
	"CHARSET",
	"CHECK",
	"CHECKPOINT",
	"CHECKSUM",
	"CIPHER",
	"CLASS_ORIGIN",
	"CLIENT",
	"CLIENT_STATISTICS",
	"CLOSE",
	"COALESCE",
	"CODE",
	"COLLATE",
	"COLLATION",
	"COLUMN",
	"COLUMN_NAME",
	"COLUMNS",
	"COLUMN_ADD",
	"COLUMN_CHECK",
	"COLUMN_CREATE",
	"COLUMN_DELETE",
	"COLUMN_GET",
	"COMMENT",
	"COMMIT",
	"COMMITTED",
	"COMPACT",
	"COMPLETION",
	"COMPRESSED",
	"CONCURRENT",
	"CONDITION",
	"CONNECTION",
	"CONSISTENT",
	"CONSTRAINT",
	"CONSTRAINT_CATALOG",
	"CONSTRAINT_NAME",
	"CONSTRAINT_SCHEMA",
	"CONTAINS",
	"CONTEXT",
	"CONTINUE",
	"CONTRIBUTORS",
	"CONVERT",
	"CPU",
	"CREATE",
	"CROSS",
	"CUBE",
	"CURRENT",
	"CURRENT_DATE",
	"CURRENT_POS",
	"CURRENT_ROLE",
	"CURRENT_TIME",
	"CURRENT_TIMESTAMP",
	"CURRENT_USER",
	"CURSOR",
	"CURSOR_NAME",
	"DATA",
	"DATABASE",
	"DATABASES",
	"DATAFILE",
	"DATE",
	"DATETIME",
	"DAY",
	"DAY_HOUR",
	"DAY_MICROSECOND",
	"DAY_MINUTE",
	"DAY_SECOND",
	"DEALLOCATE",
	"DEC",
	"DECIMAL",
	"DECLARE",
	"DEFAULT",
	"DEFINER",
	"DELAYED",
	"DELAY_KEY_WRITE",
	"DELETE",
	"DESC",
	"DESCRIBE",
	"DES_KEY_FILE",
	"DETERMINISTIC",
	"DIAGNOSTICS",
	"DIRECTORY",
	"DISABLE",
	"DISCARD",
	"DISK",
	"DISTINCT",
	"DISTINCTROW",
	"DIV",
	"DO",
	"DOUBLE",
	"DROP",
	"DUAL",
	"DUMPFILE",
	"DUPLICATE",
	"DYNAMIC",
	"EACH",
	"ELSE",
	"ELSEIF",
	"ENABLE",
	"ENCLOSED",
	"END",
	"ENDS",
	"ENGINE",
	"ENGINES",
	"ENUM",
	"ERROR",
	"ERRORS",
	"ESCAPE",
	"ESCAPED",
	"EVENT",
	"EVENTS",
	"EVERY",
	"EXAMINED",
	"EXCHANGE",
	"EXECUTE",
	"EXISTS",
	"EXIT",
	"EXPANSION",
	"EXPORT",
	"EXPLAIN",
	"EXTENDED",
	"EXTENT_SIZE",
	"FALSE",
	"FAILOVER",
	"FAST",
	"FAULTS",
	"FETCH",
	"FIELDS",
	"FILE",
	"FIRST",
	"FIXED",
	"FLOAT",
	"FLOAT4",
	"FLOAT8",
	"FLUSH",
	"FOR",
	"FORCE",
	"FOREIGN",
	"FOUND",
	"FROM",
	"FULL",
	"FULLTEXT",
	"FUNCTION",
	"GENERAL",
	"GENERATED",
	"GEOMETRY",
	"GEOMETRYCOLLECTION",
	"GET_FORMAT",
	"GET",
	"GLOBAL",
	"GOOGLESTATS",
	"GRANT",
	"GRANTS",
	"GROUP",
	"HANDLER",
	"HARD",
	"HASH",
	"HAVING",
	"HELP",
	"HIGH_PRIORITY",
	"HOST",
	"HOSTS",
	"HOUR",
	"HOUR_MICROSECOND",
	"HOUR_MINUTE",
	"HOUR_SECOND",
	"ID",
	"IDENTIFIED",
	"IDLE",
	"IF",
	"IGNORE",
	"IGNORE_SERVER_IDS",
	"IMPORT",
	"IN",
	"INDEX",
	"INDEXES",
	"INDEX_STATISTICS",
	"INFILE",
	"INITIAL_SIZE",
	"INNER",
	"INOUT",
	"INSENSITIVE",
	"INSERT",
	"INSERT_METHOD",
	"INSTALL",
	"INT",
	"INT1",
	"INT2",
	"INT3",
	"INT4",
	"INT8",
	"INTEGER",
	"INTERVAL",
	"INTO",
	"IO",
	"IO_THREAD",
	"IPC",
	"IS",
	"ISOLATION",
	"ISSUER",
	"ITERATE",
	"INVOKER",
	"JOIN",
	"KEY",
	"KEYS",
	"KEY_BLOCK_SIZE",
	"KILL",
	"LANGUAGE",
	"LAST",
	"LAST_VALUE",
	"LEADING",
	"LEAVE",
	"LEAVES",
	"LEFT",
	"LESS",
	"LEVEL",
	"LIKE",
	"LIMIT",
	"LINEAR",
	"LINES",
	"LINESTRING",
	"LIST",
	"LOAD",
	"LOCAL",
	"LOCALTIME",
	"LOCALTIMESTAMP",
	"LOCK",
	"LOCKS",
	"LOGFILE",
	"LOGS",
	"LONG",
	"LONGBLOB",
	"LONGTEXT",
	"LOOP",
	"LOW_PRIORITY",
	"MASTER",
	"MASTER_CONNECT_RETRY",
	"MASTER_GTID_POS",
	"MASTER_HOST",
	"MASTER_LOG_FILE",
	"MASTER_LOG_POS",
	"MASTER_PASSWORD",
	"MASTER_PORT",
	"MASTER_SERVER_ID",
	"MASTER_SOCKET",
	"MASTER_SSL",
	"MASTER_SSL_CA",
	"MASTER_SSL_CAPATH",
	"MASTER_SSL_CERT",
	"MASTER_SSL_CIPHER",
	"MASTER_SSL_CRL",
	"MASTER_SSL_CRLPATH",
	"MASTER_SSL_KEY",
	"MASTER_SSL_VERIFY_SERVER_CERT",
	"MASTER_USER",
	"MASTER_USE_GTID",
	"MASTER_HEARTBEAT_PERIOD",
	"MATCH",
	"MAX_ROWS",
	"MAX_SIZE",
	"MAXVALUE",
	"MEDIUM",
	"MEDIUMBLOB",
	"MEDIUMINT",
	"MEDIUMTEXT",
	"MEMORY",
	"MERGE",
	"MESSAGE_TEXT",
	"MICROSECOND",
	"MIDDLEINT",
	"MIGRATE",
	"MINUTE",
	"MINUTE_MICROSECOND",
	"MINUTE_SECOND",
	"MIN_ROWS",
	"MOD",
	"MODE",
	"MODIFIES",
	"MODIFY",
	"MONTH",
	"MULTILINESTRING",
	"MULTIPOINT",
	"MULTIPOLYGON",
	"MUTEX",
	"MYSQL_ERRNO",
	"NAME",
	"NAMES",
	"NATIONAL",
	"NATURAL",
	"NDB",
	"NDBCLUSTER",
	"NCHAR",
	"NEW",
	"NEXT",
	"NO",
	"NO_WAIT",
	"NODEGROUP",
	"NONE",
	"NOT",
	"NO_WRITE_TO_BINLOG",
	"NULL",
	"NUMBER",
	"NUMERIC",
	"NVARCHAR",
	"OFFSET",
	"OLD_PASSWORD",
	"ON",
	"ONE",
	"ONLINE",
	"ONLY",
	"OPEN",
	"OPTIMIZE",
	"OPTIONS",
	"OPTION",
	"OPTIONALLY",
	"OR",
	"ORDER",
	"OUT",
	"OUTER",
	"OUTFILE",
	"OWNER",
	"PACK_KEYS",
	"PAGE",
	"PAGE_CHECKSUM",
	"PARSER",
	"PARSE_VCOL_EXPR",
	"PARTIAL",
	"PARTITION",
	"PARTITIONING",
	"PARTITIONS",
	"PASSWORD",
	"PERSISTENT",
	"PHASE",
	"PLUGIN",
	"PLUGINS",
	"POINT",
	"POLYGON",
	"PORT",
	"PRECISION",
	"PREPARE",
	"PRESERVE",
	"PREV",
	"PRIMARY",
	"PRIVILEGES",
	"PROCEDURE",
	"PROCESS",
	"PROCESSLIST",
	"PROFILE",
	"PROFILES",
	"PROXY",
	"PURGE",
	"QUARTER",
	"QUERY",
	"QUICK",
	"RANGE",
	"READ",
	"READ_ONLY",
	"READ_WRITE",
	"READS",
	"REAL",
	"REBUILD",
	"RECOVER",
	"REDO_BUFFER_SIZE",
	"REDOFILE",
	"REDUNDANT",
	"REFERENCES",
	"REGEXP",
	"RELAY",
	"RELAYLOG",
	"RELAY_LOG_FILE",
	"RELAY_LOG_POS",
	"RELAY_THREAD",
	"RELEASE",
	"RELOAD",
	"REMOVE",
	"RENAME",
	"REORGANIZE",
	"REPAIR",
	"REPEATABLE",
	"REPLACE",
	"REPLICATION",
	"REPEAT",
	"REQUIRE",
	"RESET",
	"RESIGNAL",
	"RESTORE",
	"RESTRICT",
	"RESUME",
	"RETURNED_SQLSTATE",
	"RETURN",
	"RETURNING",
	"RETURNS",
	"REVERSE",
	"REVOKE",
	"RIGHT",
	"RLIKE",
	"ROLE",
	"ROLLBACK",
	"ROLLUP",
	"ROUTINE",
	"ROW",
	"ROW_COUNT",
	"ROWS",
	"ROW_FORMAT",
	"RTREE",
	"SAVEPOINT",
	"SCHEDULE",
	"SCHEMA",
	"SCHEMA_NAME",
	"SCHEMAS",
	"SECOND",
	"SECOND_MICROSECOND",
	"SECURITY",
	"SELECT",
	"SENSITIVE",
	"SEPARATOR",
	"SERIAL",
	"SERIALIZABLE",
	"SESSION",
	"SERVER",
	"SET",
	"SHARE",
	"SHOW",
	"SHUTDOWN",
	"SIGNAL",
	"SIGNED",
	"SIMPLE",
	"SLAVE",
	"SLAVES",
	"SLAVE_POS",
	"SLOW",
	"SNAPSHOT",
	"SMALLINT",
	"SOCKET",
	"SOFT",
	"SOME",
	"SONAME",
	"SOUNDS",
	"SOURCE",
	"SPATIAL",
	"SPECIFIC",
	"SQL",
	"SQLEXCEPTION",
	"SQLSTATE",
	"SQLWARNING",
	"SQL_BIG_RESULT",
	"SQL_BUFFER_RESULT",
	"SQL_CACHE",
	"SQL_CALC_FOUND_ROWS",
	"SQL_NO_CACHE",
	"SQL_SMALL_RESULT",
	"SQL_THREAD",
	"SQL_TSI_SECOND",
	"SQL_TSI_MINUTE",
	"SQL_TSI_HOUR",
	"SQL_TSI_DAY",
	"SQL_TSI_WEEK",
	"SQL_TSI_MONTH",
	"SQL_TSI_QUARTER",
	"SQL_TSI_YEAR",
	"SSL",
	"START",
	"STARTING",
	"STARTS",
	"STATS_AUTO_RECALC",
	"STATS_PERSISTENT",
	"STATS_SAMPLE_PAGES",
	"STATS_SERVER",
	"STATS_SERVERS",
	"STATUS",
	"STOP",
	"STORAGE",
	"STRAIGHT_JOIN",
	"STRING",
	"SUBCLASS_ORIGIN",
	"SUBJECT",
	"SUBPARTITION",
	"SUBPARTITIONS",
	"SUPER",
	"SUPPRESS_SAFETY_WARNING",
	"SUSPEND",
	"SWAPS",
	"SWITCHES",
	"TABLE",
	"TABLE_NAME",
	"TABLES",
	"TABLESPACE",
	"TABLE_STATISTICS",
	"TABLE_CHECKSUM",
	"TEMPORARY",
	"TEMPTABLE",
	"TERMINATED",
	"TEXT",
	"THAN",
	"THEN",
	"TIME",
	"TIMESTAMP",
	"TIMESTAMPADD",
	"TIMESTAMPDIFF",
	"TINYBLOB",
	"TINYINT",
	"TINYTEXT",
	"TO",
	"TRAILING",
	"TRANSACTION",
	"TRANSACTIONAL",
	"TRIGGER",
	"TRIGGERS",
	"TRUE",
	"TRUNCATE",
	"TYPE",
	"TYPES",
	"UNCOMMITTED",
	"UNDEFINED",
	"UNDO_BUFFER_SIZE",
	"UNDOFILE",
	"UNDO",
	"UNICODE",
	"UNION",
	"UNIQUE",
	"UNKNOWN",
	"UNLOCK",
	"UNINSTALL",
	"UNSIGNED",
	"UNTIL",
	"UPDATE",
	"UPGRADE",
	"USAGE",
	"USE",
	"USER",
	"USER_RESOURCES",
	"USER_STATISTICS",
	"USE_FRM",
	"USING",
	"UTC_DATE",
	"UTC_TIME",
	"UTC_TIMESTAMP",
	"VALUE",
	"VALUES",
	"VARBINARY",
	"VARCHAR",
	"VARCHARACTER",
	"VARIABLES",
	"VARYING",
	"VIA",
	"VIEW",
	"VIRTUAL",
	"WAIT",
	"WARNINGS",
	"WEEK",
	"WEIGHT_STRING",
	"WHEN",
	"WHERE",
	"WHILE",
	"WITH",
	"WORK",
	"WRAPPER",
	"WRITE",
	"X509",
	"XOR",
	"XA",
	"XML",
	"YEAR",
	"YEAR_MONTH",
	"ZEROFILL",
]
SQL_FUNC = [
	"ADDDATE",
	"BIT_AND",
	"BIT_OR",
	"BIT_XOR",
	"CAST",
	"COUNT",
	"CURDATE",
	"CURTIME",
	"DATE_ADD",
	"DATE_SUB",
	"EXTRACT",
	"GROUP_CONCAT",
	"MAX",
	"MID",
	"MIN",
	"NOW",
	"ORDERED_CHECKSUM",
	"POSITION",
	"SESSION_USER",
	"STD",
	"STDDEV",
	"STDDEV_POP",
	"STDDEV_SAMP",
	"SUBDATE",
	"SUBSTR",
	"SUBSTRING",
	"SUM",
	"SYSDATE",
	"SYSTEM_USER",
	"TRIM",
	"UNORDERED_CHECKSUM",
	"VARIANCE",
	"VAR_POP",
	"VAR_SAMP",
]


def extract_fields_fromfile(filename):
	dump = os.path.join(os.path.dirname(os.path.dirname(__file__)),filename)
	with open(dump, "r") as f:
		return sorted(set([i.upper().strip() for i in f.readlines()]))[::-1]


# query su mysql per estrarli tutti
SYS_DEF = [
	("SYS_DB", ["MYSQL", "INFORMATION_SCHEMA", "SYS", "PERFORMANCE_SCHEMA"]),
	("SYSTBL", extract_fields_fromfile("systables")),
	("SYSCOL", extract_fields_fromfile("syscolumns")),
	("SYSVAR", extract_fields_fromfile("sysvars")),
	("SYSVIEW", extract_fields_fromfile("sysviews")),
	("SYSSTORED", extract_fields_fromfile("sysroutines")),
]

USR_DEF = [
	# ("USR_DB",[]), not in our db
	("USRTBL", ["TAB"]),
	("USRCOL", ["COL1", "COL2", "COL3", "COL4", "COL5", "COL6"]),
	# ("USRVAR",[]), not in our db
	# ("USRVIEW",[]),
	# ("USRFUNC",[]),
]

NUMB_TOKENS = ["DECIMAL", "INT", "HEX", "IP_ADDR"]

TOKENS = SYMBOLS + SQL_FUNC
for i in PUNCTATION_SUB:
	TOKENS.append(i[1])
for i in SYS_DEF:
	TOKENS.append(i[0])
for i in USR_DEF:
	TOKENS.append(i[0])
for i in NUMB_TOKENS:
	TOKENS.append(i)
TOKENS.append("STR")
TOKENS.append("CHR")


def substitute_list_token(token_list, query, insert_space=False):
	for sys_token in token_list:
		replace_with = sys_token[0]
		if insert_space:
			replace_with = " " + replace_with + " "
		for i in sys_token[1]:
			query = query.replace(i, replace_with)
	return query


def substitute_sysinfo(query, insert_space=False):
	query = substitute_list_token(SYS_DEF, query, insert_space=True)
	query = substitute_list_token(USR_DEF, query, insert_space=True)
	return query


def substitute_punctation(query, insert_space=False):
	for i in PUNCTATION_SUB:
		replace_with = i[1]
		if insert_space:
			replace_with = " " + replace_with + " "
		query = query.replace(i[0], replace_with)
	return query


def sub_with_regexp(regexp, token, query, insert_space=False):
	replace_with = token
	if insert_space:
		replace_with = " " + replace_with + " "
	query = re.sub(regexp, replace_with, query)
	return query


def apply_regexp(query, insert_space=False):
	decimal_r = r"[-+]?[0-9]*\.[0-9]+"
	int_r = r"[-+]?[0-9]+"
	hex_r = r"(X'[0-9A-F]+'|0x[0-9A-F]+)"
	ip_r = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
	query = sub_with_regexp(hex_r, "HEX", query, insert_space=True)
	query = sub_with_regexp(ip_r, "IP_ADDR", query, insert_space=True)
	query = sub_with_regexp(decimal_r, "DECIMAL", query, insert_space=True)
	query = sub_with_regexp(int_r, "INT", query, insert_space=True)
	return query


def normalize_dots(query):
	query = (
		query.replace("ORDER BY STR", " ORDER BY USRCOL")
			.replace("CHR DOT USRCOL", " USRCOL")
			.replace("STR DOT USRCOL", " USRCOL")
			.replace("USRTBL DOT USRCOL", " USRCOL")
	)
	return query

import networkx as nx
import numpy as np
from sklearn.svm import SVC

def histogram_of_tokens(tokens):
    total_length = len(TOKENS)
    hist = [0 for _ in range(total_length)]
    for t in tokens:
        hist[TOKENS.index(t)] = tokens.count(t)
    return hist

class SQLiGoT(SVC):
    def __init__(
        self,
        C=100.0,
        kernel="rbf",
        degree=3,
        gamma=0.0774263682681127,
        coef0=0.0,
        shrinking=True,
        probability=True,
        tol=0.001,
        cache_size=200,
        class_weight=None,
        verbose=False,
        max_iter=-1,
        decision_function_shape="ovr",
        random_state=None,
        sliding_window_length=5,
    ):
        if sliding_window_length is None or type(sliding_window_length) != int:
            sliding_window_length = 5
        self._sliding_window_length = sliding_window_length
        super().__init__(
            C=C,
            kernel=kernel,
            degree=degree,
            gamma=gamma,
            coef0=coef0,
            shrinking=shrinking,
            probability=probability,
            tol=tol,
            cache_size=cache_size,
            class_weight=class_weight,
            verbose=verbose,
            max_iter=max_iter,
            decision_function_shape=decision_function_shape,
            random_state=random_state,
        )

    def preprocess_input_query(self, query):
        query = query.strip().upper()
        query = re.sub(r"( |\t|\n|\r|/\*\*/|`)+", " ", query)
        query = substitute_sysinfo(query, insert_space=True).strip()
        query = apply_regexp(query, insert_space=True).strip()
        query = substitute_punctation(query, insert_space=True).strip()
        query = re.sub(" +", " ", query).strip()
        query = normalize_dots(query)
        splitted_string = query.split(" ")
        tokens = []
        for t in splitted_string:
            if t in TOKENS:
                tokens.append(t)
            else:
                if len(t) > 1:
                    tokens.append("STR")
                else:
                    tokens.append("CHR")
        if "WHERE" not in tokens:
            return None
        tokens = tokens[tokens.index("WHERE") + 1 :]
        if not tokens:
            return None
        return tokens

    def create_graph_from_sql_query(self, sql_query, proportional=False, undirected=False):
        token_sequence = self.preprocess_input_query(sql_query)
        if token_sequence is None:
            return None
        graph = nx.Graph() if undirected else nx.DiGraph()
        token_count = histogram_of_tokens(token_sequence)
        [
            graph.add_node(t, count=token_count[i])
            for i, t in enumerate(TOKENS)
        ]
        for i, token in enumerate(token_sequence):
            stop_slide = (
                i + self._sliding_window_length
                if i + self._sliding_window_length < len(token_sequence)
                else len(token_sequence)
            )
            window = token_sequence[i + 1 : stop_slide]
            for j, slide_token in enumerate(window):
                additive_weight = (
                    i - j + self._sliding_window_length if proportional else 1
                )
                if graph.has_edge(token, slide_token):
                    graph[token][slide_token]["weight"] += additive_weight
                else:
                    graph.add_edge(token, slide_token, weight=additive_weight)
            if stop_slide == len(token_sequence):
                break
        return graph

    def extract_feature_vector_from_directed_graph(graph, normalize=True):
        if not isinstance(graph, nx.DiGraph):
            raise ValueError()
        allowed = TOKENS
        in_degree_dict = [graph.in_degree(t, "weight") for t in allowed]
        max_in_degree = max(in_degree_dict) if normalize else 1
        out_degree_dict = [graph.out_degree(t, "weight") for t in allowed]
        max_out_degree = max(out_degree_dict) if normalize else 1
        if max_in_degree == 0 or max_out_degree == 0:
            return None
        feature_vector = []
        [
            feature_vector.extend((a / max_in_degree, b / max_out_degree))
            for (a, b) in zip(in_degree_dict, out_degree_dict)
        ]
        feature_vector = np.array(feature_vector)
        return feature_vector

    def extract_feature_vector_from_undirected_graph(graph):
        if not isinstance(graph, nx.Graph):
            raise ValueError()
        allowed = TOKENS
        degree = [graph.degree(t, "weight") for t in allowed]
        max_degree = max(degree)
        count = [graph.node[t]["count"] for t in allowed]
        max_count = max(count)
        if max_count == 0 or max_degree == 0:
            return None
        feature_vector = []
        [
            feature_vector.extend((a / max_count, b / max_degree))
            for (a, b) in zip(count, degree)
        ]
        feature_vector = np.array(feature_vector)
        return feature_vector

    def preprocess_single_query(self, sql_query, undirected= False, proportional= True):
        graph = self.create_graph_from_sql_query(
            sql_query, proportional=proportional, undirected=undirected
        )
        if graph is None:
            return None
        extract_feat = (
            self.extract_feature_vector_from_undirected_graph
            if undirected
            else self.extract_feature_vector_from_directed_graph
        )
        feature_vector = extract_feat(graph)
        if feature_vector is None:
            return None
        return feature_vector

    def _create_feature_vectors_from_file(self, filepath, undirected=False, proportional=True, limit_samples=10000):
        X = []
        with open(filepath, "r") as f:
            sql_queries = f.readlines()
        for i, sql_query in enumerate(sql_queries):
            if limit_samples is not None and i > limit_samples:
                break
            feature_vector = self.preprocess_single_query(sql_query, undirected=undirected, proportional=proportional)
            if feature_vector is None:
                if limit_samples is not None:
                    limit_samples += 1
                continue
            X.append(feature_vector)
        X = np.array(X)
        return X

    def balance_data(self, X_a, X_b):
        max_lenght = min(len(X_a), len(X_b))
        X_a = X_a[:max_lenght]
        X_b = X_b[:max_lenght]
        return X_a, X_b

    def create_dataset(
        self,
        benign_filepath,
        sqlia_filepath,
        undirected=False,
        proportional=True,
        normalize=True,
        limit_samples=10000,
        balance=True,
        dump_to_file=True,
        check_cache=True,
        save_keyword_append="",
    ):
        kind = "undirected" if undirected else "directed"
        prop = "proportional" if proportional else "unprop"
        if (
            check_cache
            and os.path.isfile(benign_filepath)
            and os.path.isfile(sqlia_filepath)
        ):
            X_benign = np.load(benign_filepath)
            X_sqlia = np.load(sqlia_filepath)
            if balance:
                X_benign, X_sqlia = self.balance_data(X_benign, X_sqlia)
            X = np.vstack((X_benign, X_sqlia))
            y = np.ones(len(X_benign) + len(X_sqlia))
            y[: len(X_benign)] = -1
            return X, y
        else:
            X_benign = self.create_feature_vectors_from_file(
                benign_filepath,
                undirected=undirected,
                proportional=proportional,
                normalize=normalize,
                limit_samples=limit_samples,
            )
            X_sqlia = self.create_feature_vectors_from_file(
                sqlia_filepath,
                undirected=undirected,
                proportional=proportional,
                normalize=normalize,
                limit_samples=limit_samples,
            )
        X_benign = np.unique(X_benign, axis=0)
        X_sqlia = np.unique(X_sqlia, axis=0)
        np.save(
            "{}graph_{}_{}_sane.npy".format(save_keyword_append, kind, prop), X_benign
        )
        np.save(
            "{}graph_{}_{}_sqlia.npy".format(save_keyword_append, kind, prop), X_sqlia
        )
        if balance:
            X_benign, X_sqlia = self.balance_data(X_benign, X_sqlia)
        X = np.vstack((X_benign, X_sqlia))
        y = np.ones(len(X_benign) + len(X_sqlia))
        y[: len(X_benign)] = -1
        return X, y
