done = function(summary, latency, requests)

    date = os.date("%Y-%m-%d_%H:%M:%S")
    file_name = "benchmark/wrk_results/results_" .. date .. ".txt"
    file = io.open(file_name, "w")
    io.output(file)

    micro_sec_to_sec_rate = 1000000
    micro_to_mili_sec_rate = 1000

    l50 = latency:percentile(50)/micro_to_mili_sec_rate
    l75 = latency:percentile(75)/micro_to_mili_sec_rate
    l90 = latency:percentile(90)/micro_to_mili_sec_rate
    l99 = latency:percentile(99.99)/micro_to_mili_sec_rate
    avg = latency.mean
    time_seconds = summary.duration/micro_sec_to_sec_rate
    rps = summary.requests/time_seconds
    timeouts = summary.errors.timeout

    io.write("| 50%(ms) | 75%(ms) | 90%(ms) | 99.99%(ms) | Avg(ms) | Req/s | Timeouts | Date |\n")
    io.write(string.format("| %0.2f | %0.2f | %0.2f | %0.2f | %0.2f | %0.2f | %d | %s |", l50, l75, l90,l99, avg, rps, timeouts, date))
    io.close(file)
end
