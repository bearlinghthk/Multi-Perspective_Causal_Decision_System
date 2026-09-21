# Generic Closed Investigation

This example completes three deterministic cycles:

此 example 完成三個 deterministic cycles：

1. Query processing state.
2. Query whether a response was created.
3. Query whether the response was delivered.

The configured evidence is:

```text
processing_state = completed
response_created = true
response_delivered = false
```

The investigation progressively falsifies:

```text
received_not_completed
completed_no_response
response_delivered_state_not_updated
```

and stops with:

```text
response_created_not_delivered
```

The remaining model is resolved only within the current candidate set and
scope. It is not declared universally true.

最後剩下的 model 只代表在目前 candidate set 及 scope 內得到解決，並不代表
已被普遍證明為真。
