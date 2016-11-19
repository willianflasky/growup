#!/usr/bin/env python3

import os,sys
print(os.path.basename(__file__))

print(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,"/Users/willian/PycharmProjects/s12_python3/day5")

info={'aof_rewrite_in_progress': 0, 'total_connections_received': 148, 'used_cpu_sys_children': 0.0, 'run_id': '61ca9b8668d10b487fb3217ff1ed76c2f4aefb5e', 'rejected_connections': 0, 'redis_build_id': 0, 'used_memory_peak_human': '4.78M', 'pubsub_patterns': 0, 'redis_mode': 'standalone', 'connected_slaves': 1, 'uptime_in_days': 1, 'multiplexing_api': 'epoll', 'lru_clock': 15210979, 'redis_version': '2.8.24', 'redis_git_sha1': 0, 'sync_partial_ok': 0, 'gcc_version': '0.0.0', 'repl_backlog_size': 1048576, 'connected_clients': 5, 'keyspace_misses': 2, 'used_memory': 4827520, 'tcp_port': 6379, 'master_repl_offset': 10722966, 'used_cpu_user_children': 0.0, 'repl_backlog_first_byte_offset': 9674391, 'rdb_current_bgsave_time_sec': -1, 'pubsub_channels': 0, 'used_cpu_user': 34.86, 'used_memory_lua': 36864, 'instantaneous_ops_per_sec': 3, 'rdb_last_save_time': 1457931601, 'total_commands_processed': 439475, 'aof_last_write_status': 'ok', 'role': 'master', 'aof_rewrite_scheduled': 0, 'sync_partial_err': 1, 'used_memory_rss': 6770688, 'hz': 10, 'sync_full': 2, 'aof_enabled': 0, 'config_file': '/etc/redis.conf', 'used_cpu_sys': 33.98, 'rdb_last_bgsave_status': 'ok', 'instantaneous_output_kbps': 0.07, 'latest_fork_usec': 159, 'aof_last_bgrewrite_status': 'ok', 'aof_last_rewrite_time_sec': -1, 'used_memory_human': '4.60M', 'loading': 0, 'blocked_clients': 0, 'process_id': 1, 'db0': {'keys': 2, 'expires': 0, 'avg_ttl': 0}, 'repl_backlog_histlen': 1048576, 'client_biggest_input_buf': 0, 'aof_current_rewrite_time_sec': -1, 'arch_bits': 64, 'repl_backlog_active': 1, 'mem_fragmentation_ratio': 1.4, 'rdb_last_bgsave_time_sec': -1, 'expired_keys': 0, 'total_net_input_bytes': 18965755, 'evicted_keys': 0, 'rdb_bgsave_in_progress': 0, 'slave0': {'ip': '172.16.1.24', 'state': 'online', 'lag': 0, 'port': 6379, 'offset': 10722966}, 'instantaneous_input_kbps': 0.13, 'client_longest_output_list': 0, 'mem_allocator': 'jemalloc-3.6.0', 'total_net_output_bytes': 127056298, 'used_memory_peak': 5010912, 'uptime_in_seconds': 119954, 'rdb_changes_since_last_save': 119955, 'redis_git_dirty': 0, 'os': 'Amazon ElastiCache', 'keyspace_hits': 3}

for k,v in info.items():
    print(k,v)
